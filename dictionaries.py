stuff = {"food": 12, "energy": 100, "alies": 3}

#print(stuff.get("food"))

# print(stuff.items())

#print(stuff.keys())

"""
print(stuff.popitem())
print(stuff)

print(stuff.setdefault("food"))
print(stuff)

print(stuff.setdefault("capacity", 36))
print(stuff)
"""

new_items = {"rocks": 23, "arrows": 8}
print(stuff.update(new_items))
print(stuff)

up_new = {"food": 973}

stuff.update(up_new)

print(stuff)

stuff.update(rocks=8, alies=9)
print(stuff)
