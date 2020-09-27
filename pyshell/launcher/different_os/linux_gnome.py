import subprocess
from launcher.abstract_os import AbstractOS


class LinuxGnome(AbstractOS):
    def browser(self):
        subprocess.call('gedit')

    def filemanager(self):
        subprocess.call('nautilus')

    def note(self):
        subprocess.call('gedit')

    def calc(self):
        subprocess.call('gnome-calculator')
