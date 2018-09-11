
from math import sqrt

def get_sides(side='d'):
    sides = {
        'a': 'b or c',
        'b': 'a or c',
        'c': 'a or b',
        'd': 'a, b or c'
    }[side]
    a = input("Choose a side, %s: " % sides)
    return a 

def get_hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)

def get_side(k, h):
    return sqrt(h ** 2 - k ** 2)
    
def get_data(side):
    return float(raw_input("Enter a value for side %s: " % side)) 

a, b, c = ('a', 'b', 'c')

sides = {}

s_1 = get_sides()
s_2 = get_sides(s_1)

sides[s_1] = get_data(s_1)
sides[s_2] = get_data(s_2)

if c not in sides.keys():
    sides[c] = get_hypotenuse(sides[a], sides[b])
    side = c
elif b not in sides.keys():
    sides[b] = get_side(sides[a], sides[c])
    side = b
else:
    sides[a] = get_side(sides[b], sides[c])
    side = a

print "Given side %s = %r, and side %s = %r, \
\nthe measure of the unknown side, %s, is %r" \
% (s_1, sides[s_1], s_2, sides[s_2], side, sides[side])

