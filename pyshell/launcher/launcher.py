import os
import platform

from .abstract_os import AbstractOS
from .linux import LinuxGnome, LinuxKDE
from .windows import Windows


class Launcher(AbstractOS):
    def __init__(self):
        os_type = platform.system()

        if os_type == 'Linux':
            # Можно использовать DESKTOP_SESSION,
            # XDG_SESSION_DESKTOP и XDG_CURRENT_DESKTOP
            # т.к это практически одно и то же.
            linux_de = os.environ['XDG_CURRENT_DESKTOP']

            if linux_de == 'GNOME':
                self.__os = LinuxGnome()
            elif linux_de == 'KDE':
                self.__os = LinuxKDE()
        elif os_type == 'Windows':
            windows_rls = platform.release()

            if windows_rls == '10' or windows_rls == '7':
                self.__os = Windows()
            # elif windows_rls == 'XP':
                # self.__os = WindowsXP()

    def note(self):
        self.__os.note()

    def calc(self):
        self.__os.calc()

    def browser(self):
        self.__os.browser()

    def filemanager(self):
        self.__os.filemanager()

    def sysmonitor(self):
        self.__os.sysmonitor()
