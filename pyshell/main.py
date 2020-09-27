import os
import platform
from launcher.current_os_enum import CurrentOS
from launcher.launcher import Launcher


def define_os():
    current_os = platform.system()

    if current_os == 'Linux':
        # Можно использовать DESKTOP_SESSION,
        # XDG_SESSION_DESKTOP и XDG_CURRENT_DESKTOP
        # т.к это практически одно и то же.
        linux_de = os.environ['XDG_CURRENT_DESKTOP']

        if linux_de == 'GNOME':
            return CurrentOS.linux_gnome
        elif linux_de == 'KDE':
            pass
    elif current_os == 'Windows':
        print(platform.win32_ver())


if __name__ == '__main__':
    os = define_os()

    launcher = Launcher(os)

    command = input('shell> ')

    if command == 'filemanager':
        launcher.filemanager()
