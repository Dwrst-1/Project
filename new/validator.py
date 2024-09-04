import re

from new.exceptions import ValidationError


class Validator:
    @staticmethod
    def validate_mail(login):
        mail_mask = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(mail_mask,login) is None:
            raise ValidationError('Неверный логин')
        return True
    @staticmethod
    def validate_password(password):
        passw_mask = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|]).{4,}'
        if re.fullmatch(passw_mask,password) is None:
            raise ValidationError('Неверный пароль')
        return True





