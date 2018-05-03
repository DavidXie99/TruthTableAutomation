def imp(prop1,prop2):
    if prop1:
        return prop2
    return True

def inf(prop1,prop2):
    if prop1:
        return True
    return not prop2

def iff(prop1,prop2):
    return prop1 == prop2
