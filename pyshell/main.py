import readline
from launcher import Launcher

COMMANDS = ['note', 'calc', 'browser', 'filemanager', 'sysmonitor', 'exit']


def complete(text, state):
    for cmd in COMMANDS:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1


if __name__ == '__main__':
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
        elif command == 'sysmonitor':
            launcher.sysmonitor()
        else:
            break
