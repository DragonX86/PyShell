import subprocess
import webbrowser

from ..abstract_os import AbstractOS


class Windows(AbstractOS):
    def note(self):
        subprocess.Popen('notepad.exe')

    def calc(self):
        subprocess.Popen('calc.exe')

    def browser(self):
        webbrowser.open("https://yandex.ru/")

    def filemanager(self):
        subprocess.Popen('explorer.exe')
