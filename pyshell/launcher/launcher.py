import os
import platform

from .abstract_os import AbstractOS
from .linux import Gnome
from .windows import Windows


class Launcher(AbstractOS):
    def __init__(self):
        if platform.system() == 'Linux':
            linux_de = os.environ['XDG_CURRENT_DESKTOP']

            if linux_de == 'GNOME':
                self.__os = Gnome()
            # elif linux_de == 'KDE':
            #     self.__os = LinuxKDE()
        elif platform.system() == 'Windows':
            windows_rls = platform.release()

            if windows_rls == '10' or windows_rls == '7':
                self.__os = Windows()

    def notepad(self):
        self.__os.notepad()

    def calculator(self):
        self.__os.calculator()

    def browser(self):
        self.__os.browser()

    def filemanager(self):
        self.__os.filemanager()

    def sysmonitor(self):
        self.__os.sysmonitor()

    def execute(self):
        self.__os.execute()

    def dispatch(self, value):
        method_name = str(value)
        method = getattr(self, method_name)
        method()
