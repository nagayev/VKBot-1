from ._base_import import *


def cmd_wop():
    s = ''
    for text in message['fwd_messages']:
        s += ''.join(map(lambda x: keys_wop[x] if x in keys_wop else x, text['body']))
    '\n\n'.join()
