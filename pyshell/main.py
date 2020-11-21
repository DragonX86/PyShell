import os
import readline

from launcher import Launcher

COMMANDS = ['notepad', 'calculator', 'browser', 'filemanager', 'sysmonitor', 'execute', 'exit']


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
        command = input('shell> ').split(' ')

        if command[0] != 'exit':
            if len(command) > 1:
                c = 2
                text_command = ""
                while c < len(command):
                    text_command += command[c] + " "
                    c += 1

                os.environ['COMMAND'] = command[1]
                os.environ['ARGS'] = text_command
            launcher.dispatch(command[0])
        else:
            exit(0)
