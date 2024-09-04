import json
import os.path
from datetime import datetime, UTC
from validator import Validator
from new.exceptions import AuthorizationError, RegistrationError


class Authenticator:
    def __init__(self):
        self.login: str | None = None
        self._password: str
        self.last_success_login_at: datetime | None
        self.errors_count: int = 0
        if self._is_auth_file_exist():
            self._read_auth_file()
    def _is_auth_file_exist(self):
        return os.path.exists('auth.json')

    def _read_auth_file(self):
        with open('auth.json') as a:
            inform = json.load(a)
        self.login = inform['login']
        self.password = inform['password']
        self.last_success_login_at = datetime.fromisoformat(inform['time'])
        self.errors_count = inform['errors']

    def authorize(self, login, password):
        if login == self.login and password == self.password:
            self._update_auth_file()
        else:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorizationError('Неверный логин и/или пароль')
        if self.login is None:
            raise AuthorizationError('Неверный логин и/или пароль')

    def _update_auth_file(self):
        data = {'login': self.login, 'password': self.password, 'time': datetime.now(tz=UTC).isoformat(), 'errors': self.errors_count}
        with open('auth.json', 'w') as au:
            json.dump(data, au)

    def registrate(self, login, password):
        if self.login is not None:
            raise RegistrationError('Ты не прошел регистрацию')
        if self._is_auth_file_exist():
            raise RegistrationError('Ты не прошел регистрацию')
        if Validator.validate_mail(login) and Validator.validate_password(password):
            self.login = login
            self.password = password
            self.last_success_login_at = datetime.isoformat(datetime.now(tz=UTC))
            self.errors_count = 0
            self._update_auth_file()







