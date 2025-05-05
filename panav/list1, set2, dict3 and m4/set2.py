# set2.py
def slen2(s):
    return len(s)

def adds2(s, x):
    s.add(x)
    return s

def remove2(s, x):
    try:
        s.remove(x)
        return s
    except KeyError:
        return f"Error: {x} not found in set."