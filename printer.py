import win32api
import datetime


class LazyPrinter:

    def __init__(self):
        pass

    def print_file(self, file_path):
        try:
            win32api.ShellExecute(2, 'print', file_path, None, None, 0)
        except Exception as error:
            with open(r'.\data\errors.txt', 'a') as file:
                error_dt = datetime.datetime.now().strftime('%Y.%m.%d %H:%M')
                file.write(f'{error_dt} - {error}\n')
