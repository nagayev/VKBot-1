def return_param(**var):
    import json
    with open('returns_params.json', 'r+') as file:
        file.write(json.dumps(var, indent=4))
