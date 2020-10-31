import os


def exist_program(command: str):
    if type(command) != str:
        raise TypeError('The argument passed is not a string.')
    elif len(command.strip()) == 0:
        raise ValueError('Empty string was passed.')

    paths = os.environ['PATH'].split(':')

    for path in paths:
        if os.path.exists(os.path.join(path, command)):
            return True

    return False
