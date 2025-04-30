import docker
import tempfile
import os

client = docker.from_env()

with open('./test.py', 'r') as f:
    code = f.read()
with open('./test1.py', 'r') as f:
    test_code = f.read()
print(code)
try:
    with tempfile.TemporaryDirectory() as temp_dir:
        user_file_path = os.path.join(temp_dir, 'main.py')
        with open(user_file_path, 'w') as f:
            f.write(code)
        test_file_path = os.path.join(temp_dir, 'test_code.py')
        with open(test_file_path, 'w') as f:
            f.write(test_code)
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
        print("####### output #########  ", output)
except Exception as e:
    raise(e)