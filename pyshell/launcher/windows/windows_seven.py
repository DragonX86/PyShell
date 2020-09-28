import subprocess
from launcher.abstract_os import AbstractOS


class WindowsSeven(AbstractOS):
    def note(self):
        subprocess.call('notepad.exe')

    def calc(self):
        pass

    def browser(self):
        pass

    def filemanager(self):
        print('w7')
        subprocess.call('explorer.exe')
