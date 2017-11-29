import os
import json
jsons = {}


def update_param(params=os.listdir(os.curdir)):
    for i in params:
        if os.path.isfile(i) and i.endswith('.json'):
            exec("%s = %s" % (i[:-5], json.load(open(i))))
            jsons[i[:-5]] = eval(i[:-5])


def add_param(name, value):
    with open(name+'.json', 'r+') as file:
        file.write(json.load(value))
    update_param(name+'.json')


update_param()
