import time
logFile = '.logs/'+time.strftime("%d.%m.%Y %H:%M")+'.log'


def print_log(*args, sep=' ', end='\n', file=logFile):
    import time
    print(time.strftime("[%d.%m.%Y %H:%M:%S]: ")+sep.join(args)+end, sep='', end='')
    print(time.strftime("[%d.%m.%Y %H:%M:%S]: ")+sep.join(args)+end, sep='', end='',
          file=file)
