from collections import defaultdict, deque
from functools import lru_cache


def parse():
    with open("./data/day02.txt", "r") as file:
        ip =  file.read().strip()
        c = ip.split(",")
        x = [(int(p.split("-")[0]), int(p.split("-")[1])) for p in c]
        return x

def part12(c):
    r1,r2 = 0, 0
    for x in c:
        xx, yy = findx(x)
        r1 += xx
        r2 += yy

    print(r1, r2)

def findx(x):
    r1,r2 = [], []
    (a,b) = x
    for i in range(a,b+1):
        if is_invalid_part1(i):
            r1.append(i)
        if is_invalid_part2(i):
            r2.append(i)
    # print(f"For range {x} invalid ids are {r2}")
    return sum(r1), sum(r2)


def is_invalid_part2(i):
    return is_repeat(str(i))

def is_invalid_part1(i):
    s = str(i)
    if len(s)%2 == 1:
        return False
    return all_same(s) or is_repeat_twice(s)

def all_same(s):
    if len(s) == 1:
        return False
    x = s[0]
    for i in range(1,len(s)):
        if s[i] != x:
            return False
    return True

def is_repeat_twice(s):
    mid = len(s) // 2
    a , b = s[mid:] , s[:mid]
    for i in range(len(b)):
        if a[i] != b[i]:
            return False
    return True
@lru_cache
def is_repeat(s):
    if len(s) == 1:
        return False
    for i in range(1, len(s)//2 + 1):
        sub = []
        for j in range(0, len(s), i):
            sub.append(s[j:j+i])
        if all_sub_equal(sub):
            return True
    return False

def all_sub_equal(sub):
    x = sub[0]
    for i in range(1,len(sub)):
        if sub[i] != x:
            return False
    return True


c = parse()
part12(c)

