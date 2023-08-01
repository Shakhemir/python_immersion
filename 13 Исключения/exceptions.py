class UserException(Exception):
    pass


class PositiveIntError(UserException):
    def __str__(self):
        return 'Число должно быть положительным'


class JSONFileNameError(Exception):
    def __init__(self, file_name):
        self.json_file_name = file_name

    def __str__(self):
        return f'Неправильное имя файла "{self.json_file_name}"'
