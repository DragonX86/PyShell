import readline
from launcher import Launcher
from utils import define_os

COMMANDS = ['note', 'calc', 'browser', 'filemanager', 'taskmanager', 'exit']


def complete(text, state):
    for cmd in COMMANDS:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1


if __name__ == '__main__':
    define_os()
    launcher = Launcher()

    readline.parse_and_bind('tab: complete')
    readline.set_completer(complete)

    while True:
        command = input('shell> ')

        if command == 'note':
            launcher.note()
        elif command == 'calc':
            launcher.calc()
        elif command == 'browser':
            launcher.browser()
        elif command == 'filemanager':
            launcher.filemanager()
        elif command == 'taskmanager':
            launcher.taskmanager()
        else:
            break
