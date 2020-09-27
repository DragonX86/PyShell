import subprocess
from launcher.abstract_os import AbstractOS


class LinuxGnome(AbstractOS):
    def note(self):
        subprocess.call('gedit')

    def calc(self):
        subprocess.call('gnome-calculator')
