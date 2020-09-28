import subprocess
from launcher.abstract_os import AbstractOS


class LinuxGnome(AbstractOS):
    def browser(self):
        subprocess.call('gedit')

    def filemanager(self):
        subprocess.Popen('nautilus', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def note(self):
        subprocess.Popen('gedit', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def calc(self):
        subprocess.Popen('gnome-calculator', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
