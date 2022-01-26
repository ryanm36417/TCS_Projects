
def addup(limit, x, y, total):
    if total == limit:
        return True
    elif total > limit:
        return False
    else:
        result1 = addup(limit, x, y, total + x)
        result2 = addup(limit, x, y, total + y)
        return result1 or result2


print(addup(11, 2, 3, 0))
print(addup(10, 5, 3, 0))
print(addup(8, 3, 6, 0))
print(addup(19, 5, 7, 0))
print(addup(13, 4, 2, 0))


# returns true or false is there exists a combination of x and/or y numbers that add up to a limit






