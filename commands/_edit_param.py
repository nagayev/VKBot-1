def edit(**var):
    import json
    with open('params.json', 'r+') as file:
        file.write(json.dumps(var, indent=4))