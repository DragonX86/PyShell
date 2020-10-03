import subprocess
import webbrowser
from ..abstract_os import AbstractOS


class LinuxGnome(AbstractOS):
    def note(self):
        subprocess.Popen(
            'gedit',
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def calc(self):
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
