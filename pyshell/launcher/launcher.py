from .current_os_enum import CurrentOS
from .different_os.linux_gnome import LinuxGnome
from .abstract_os import AbstractOS


class Launcher(AbstractOS):
    def __init__(self, type_os: CurrentOS = CurrentOS.default):
        if isinstance(type_os, CurrentOS):
            if type_os == CurrentOS.linux_gnome:
                self.__os = LinuxGnome()
            elif type_os == CurrentOS.linux_gnome:
                pass
            elif type_os == CurrentOS.windows_10:
                pass
            elif type_os == CurrentOS.windows_7:
                pass

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
