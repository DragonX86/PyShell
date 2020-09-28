import subprocess
from launcher.abstract_os import AbstractOS


class WindowsTen(AbstractOS):
    def note(self):
        subprocess.Popen('notepad.exe')

    def calc(self):
        subprocess.Popen('calc.exe')

    def browser(self):
        pass

    def filemanager(self):
        subprocess.Popen('explorer.exe')
