import os
import platform
from launcher.launcher import TypeOS


def define_os():
    current_os = platform.system()

    if current_os == 'Linux':
        linux_de = os.environ['XDG_CURRENT_DESKTOP']

        if linux_de == 'GNOME':
            return TypeOS.linux_gnome
        elif linux_de == 'KDE':
            pass
    elif current_os == 'Windows':
        print(platform.win32_ver())


if __name__ == '__main__':
    define_os()
