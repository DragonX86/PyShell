import os
from .linux.linux_gnome import LinuxGnome
from .linux.linux_kde import LinuxKde
from .windows.windos_ten import WindowsTen
from .windows.windows_seven import WindowsSeven
from .abstract_os import AbstractOS


class Launcher(AbstractOS):
    def __init__(self):
        if 'CURRENT_OS' in os.environ:
            if os.environ['CURRENT_OS'] == 'LINUX_GNOME':
                self.__os = LinuxGnome()
            elif os.environ['CURRENT_OS'] == 'LINUX_KDE':
                self.__os = LinuxKde()
            elif os.environ['CURRENT_OS'] == 'WINDOWS_10':
                self.__os = WindowsTen()
            elif os.environ['CURRENT_OS'] == 'WINDOWS_7':
                self.__os = WindowsSeven()
        else:
            raise ValueError

    def note(self):
        self.__os.note()

    def calc(self):
        self.__os.calc()

    def browser(self):
        self.__os.browser()

    def filemanager(self):
        self.__os.filemanager()
