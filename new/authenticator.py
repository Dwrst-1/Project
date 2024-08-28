import os.path
from datetime import datetime

from new.exceptions import AuthorizationError, RegistrationError


class Authenticator:
    def __init__(self):
        self.login: str
        self._password: str
        self.last_success_login_at: datetime | None
        self.errors_count: int = 0
        if self._is_auth_file_exist():
            self._read_auth_file()
    def _is_auth_file_exist(self):
        return os.path.exists('auth.txt')

    def _read_auth_file(self):
        with open('auth.txt','r') as a:
            self.login = a.readline().strip('\n')
            self.password = a.readline().strip('\n')
            last_login_str = a.readline().strip('\n')
            if last_login_str:
                try:
                    self.last_success_login_at = datetime.fromisoformat(last_login_str)
                except ValueError:
                    print("Ошибка формата даты в файле. Устанавливаем значение по умолчанию.")
                    self.last_success_login_at = None
            else:
                self.last_success_login_at = None
            self.errors_count = a.readline().strip('\n')

    def authorize(self, login, password):
        if login == self.login and password == self.password:
            self.last_success_login_at = datetime.utcnow()
            self.errors_count = 0
            self._update_auth_file()
        else:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorizationError
        if self.login is None:
            raise AuthorizationError

    def _update_auth_file(self,last_success_login_at,errors_count):
        with open ('auth.txt','r') as au:
            lines = au.readlines()
        lines[2] = f'{last_success_login_at}\n'
        lines[3] = f'{errors_count}\n'
        with open ('auth.txt','w') as au:
            au.writelines(lines)


    def registrate(self, login, password):
        if self._is_auth_file_exist:
            raise RegistrationError
        self.login = login
        self.password = password
        self.last_success_login_at = datetime.utcnow()
        self.errors_count = 0
        self._update_auth_file()

        if self.login is not None:
            raise RegistrationError




