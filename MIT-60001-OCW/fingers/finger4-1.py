def isIn (a,b):
    """Compares two strings to see if one is in the other"""
    return a in b or b in a

print(isIn("bin", "robbin"))
print(isIn("fast", "slow"))
print(isIn("racecar", "racecar"))
