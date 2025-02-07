import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def phone_number_validate(phone_number):
    reg = r'^09[0-9]{9}$'
    p = re.compile(reg)
    if p.match(phone_number):
        return True
    return False

def str_has_number(password):
    regex = re.compile('[0-9]')
    if regex.search(password) is None:
        raise ValidationError(_("password much include numbers"), 
                               code="password_must_include_number")
    
def str_has_letter(password):
    regex = re.compile('[a-zA-Z]')
    if regex.search(password) is None:
        raise ValidationError(_("password much include letter"), 
                               code="password_must_include_letter")

def str_has_special_char(password):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(password) is None:
        raise ValidationError(_("password much include special char"), 
                               code="password_must_include_special_char")