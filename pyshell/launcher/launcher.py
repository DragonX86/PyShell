import os
from .abstract_os import AbstractOS
from .linux import LinuxGnome, LinuxKde
from .windows import Windows


class Launcher(AbstractOS):
    def __init__(self):
        if 'CURRENT_OS' in os.environ:
            if os.environ['CURRENT_OS'] == 'LINUX_GNOME':
                self.__os = LinuxGnome()
            elif os.environ['CURRENT_OS'] == 'LINUX_KDE':
                self.__os = LinuxKde()
            elif os.environ['CURRENT_OS'] == 'WINDOWS':
                self.__os = Windows()
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

    def taskmanager(self):
        self.__os.taskmanager()
