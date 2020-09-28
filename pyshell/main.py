import os
import platform
from launcher.launcher import Launcher


def define_os():
    os_type = platform.system()

    if os_type == 'Linux':
        # Можно использовать DESKTOP_SESSION,
        # XDG_SESSION_DESKTOP и XDG_CURRENT_DESKTOP
        # т.к это практически одно и то же.
        linux_de = os.environ['XDG_CURRENT_DESKTOP']

        if linux_de == 'GNOME':
            os.environ['CURRENT_OS'] = 'LINUX_GNOME'
        elif linux_de == 'KDE':
            os.environ['CURRENT_OS'] = 'LINUX_KDE'
    elif os_type == 'Windows':
        windows_rls = platform.release()
        print(windows_rls)
        if windows_rls == '10':
            os.environ['CURRENT_OS'] = 'WINDOWS_10'
        elif windows_rls == '7':
            os.environ['CURRENT_OS'] = 'WINDOWS_7'
        elif windows_rls == 'XP':
            os.environ['CURRENT_OS'] = 'WINDOWS_XP'


if __name__ == '__main__':
    define_os()
    launcher = Launcher()


    while True:
        command = input('shell> ')

        if command == 'note':
            launcher.note()
        elif command == 'calc':
            launcher.calc()
        elif command == 'filemanager':
            launcher.filemanager()
        else:
            break
