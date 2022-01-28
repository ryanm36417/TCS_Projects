# 1
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

# 2

def one_through_ten(total):
    if total > 10:
        return
    else:
        print(total)
        total += 1
        one_through_ten(total)


one_through_ten(0)


# 3

def idk(total, limit):
    if total > limit:
        return
    else:
        print(total)
        total += 1
        idk(total, limit)


idk(0, 1)


# 4

def can_reach_zero(num):
    if num <= 1:
        return True
    elif num % 10 == 0:
        return False
    else:
        strnum = str(num)
        char_array = [int(c) for c in strnum]
        total = sum(char_array)
        total = num // total
        return can_reach_zero(total)


print("\n" * 4)

for i in range(1, 200):
    print(can_reach_zero(i), i)

