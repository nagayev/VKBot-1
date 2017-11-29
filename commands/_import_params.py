import json

PARAMS = json.load(open('param.json'))

for i in PARAMS:
    exec("%s = %s" % (i, PARAMS[i]))
