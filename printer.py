import win32api



class LazyPrinter:

    def __init__(self):
        pass

    def print_file(self, file_path):
        win32api.ShellExecute(2, 'print', file_path, None, None, 0)