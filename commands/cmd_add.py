from ._base_import import *


def cmd_add():
    if cmd[0] and cmd[0] == 'admin':
        if cmd[1] and cmd[1].isdigit():
            return "@Eadmins.append(int(cmd[1]))"
        elif cmd[1]:
            return '@EId пользователя дожен состоять только из чисел.'
        else:
            return '@!Введите id нового администратора для бота, выполнив команду по типу "/add admin {id пользователя}".'
    else:
        return "@EsendBack(helpcmd, message)"
