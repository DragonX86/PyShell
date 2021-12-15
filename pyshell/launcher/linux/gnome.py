import os
import subprocess
import webbrowser

from .utils import exist_program
from ..abstract_os import AbstractOS


class Gnome(AbstractOS):
    def notepad(self):
        subprocess.Popen(
            'gedit',
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def calculator(self):
        subprocess.Popen(
            'gnome-calculator',
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def browser(self):
        webbrowser.open("https://yandex.ru/")

    def filemanager(self):
        subprocess.Popen(
            'nautilus',
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def sysmonitor(self):
        subprocess.Popen(
            'gnome-system-monitor',
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def execute(self):
        try:
            if exist_program(os.environ.get('COMMAND')):
                os.system(os.environ.get('COMMAND') + " " + os.environ.get('ARGS'))
            else:
                print('Такой программы не существует')
        except ValueError:
            print('аргумент не был переданн')

        
