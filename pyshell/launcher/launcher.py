import enum
from .different_os.linux_gnome import LinuxGnome


class TypeOS(enum.Enum):
    linux_gnome = 0
    linux_kde = 1
    windows_10 = 2
    windows_7 = 3
    default = 99


class Launcher:
    def __init__(self, type_os: TypeOS = TypeOS.default):
        if isinstance(type_os, TypeOS):
            if type_os == TypeOS.linux_gnome:
                self.__os = LinuxGnome()
            elif type_os == TypeOS.linux_gnome:
                pass
            elif type_os == TypeOS.windows_10:
                pass
            elif type_os == TypeOS.windows_7:
                pass

        else:
            raise ValueError

    def note(self):
        self.__os.note()
