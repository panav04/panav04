# list1.py
def append1(lst, x):
    lst.append(x)
    return lst

def extend1(lst, l):
    lst.extend(l)
    return lst

def pop1(lst):
    return lst.pop() if lst else "Error: List is empty."

def remove1(lst, x):
    try:
        lst.remove(x)
        return lst
    except ValueError:
        return f"Error: {x} not found in list."