import subprocess
import webbrowser

from ..abstract_os import AbstractOS


class Windows(AbstractOS):
    def notepad(self):
        subprocess.Popen('notepad.exe')

    def calculator(self):
        subprocess.Popen('calc.exe')

    def browser(self):
        webbrowser.open("https://yandex.ru/")

    def filemanager(self):
        subprocess.Popen('explorer.exe')

    def sysmonitor(self):
        subprocess.Popen('Taskmgr.exe')

    def execute(self):
        pass
