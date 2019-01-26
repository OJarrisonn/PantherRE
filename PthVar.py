Vars = {'TRUE': True, 'FALSE': False}


def getVar(name):
    return Vars[name]


def setVar(name, value):
    if value in Vars:
        value = Vars.get(value)
    elif value.isnumeric():
        value = float(value)
    Vars[name] = value
