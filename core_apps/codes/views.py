from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import tempfile
import docker
import os

from core_apps.tutorials.models import UserProgress

# اتصال به Docker Daemon میزبان
client = docker.from_env()


from .serializers import InputOutputSerializer, CodeSerializer, SubCodeSerializer, AnswerUserSerializer, UserCodeSerializer
from .models import InputOutput, Code, SubCode, AnswerUser


class AllCodeSubject(APIView):
    def get(self, request, subject_id):
        codes = Code.objects.filter(subject_id=subject_id).prefetch_related('sub_codes')
        return Response(CodeSerializer(codes, many=True).data, status=200)


class SubCodeView(APIView):
    def get(self, request, sub_code_id):
        sub_code = SubCode.objects.get(id=sub_code_id)
        return Response(SubCodeSerializer(sub_code).data, status=200)


class TestUserCode(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def post(self, request, pk):
        sub_code = SubCode.objects.get(id=pk)

        serializers = UserCodeSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user_code_file = serializers.validated_data.get('user_code')
        user_code = user_code_file.read()
        test_code_file = sub_code.test_code
        test_code = test_code_file.read()

        try:
            with tempfile.TemporaryDirectory() as temp_dir:

                # ذخیره کد کاربر
                user_file_path = os.path.join(temp_dir, 'main.py')
                with open(user_file_path, 'w') as f:
                    f.write(user_code.decode("utf-8"))

                # # ذخیره کد تست
                test_file_path = os.path.join(temp_dir, 'test_code.py')
                with open(test_file_path, 'w') as f:
                    f.write(test_code.decode("utf-8"))

                # اجرای کانتینر Sandbox
                container = client.containers.run(
                        'python-sandbox',
                        volumes={temp_dir: {'bind': '/app', 'mode': 'rw'}},
                        command=['python', 'test_code.py'],
                        mem_limit='128m',
                        network_disabled=True,
                        remove=True,
                        stdout=True,
                        stderr=True,
                        detach=False
                    )

                output = container.decode('utf-8').strip()
                print("##########", output)
                if "OK" in output:  # فرض می‌کنیم تست اینو چاپ می‌کنه
                    self.update_progress(request.user, sub_code)
                    return Response({"correct": True, "output": output}, status=status.HTTP_200_OK)
                return Response({"correct": False, "output": output}, status=status.HTTP_200_OK)

        except docker.errors.ContainerError as e:
            error_output = e.stderr.decode('utf-8') if e.stderr else str(e)
            return Response({"correct": False, "error": error_output}, status=status.HTTP_400_BAD_REQUEST)
        except docker.errors.ImageNotFound:
            return Response({"error": "Docker image not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update_progress(self, user, sub_code):
        progress, created = AnswerUser.objects.get_or_create(user=user, topic=sub_code)
        if not progress.completed:
            progress.is_correct = True
            progress.save()