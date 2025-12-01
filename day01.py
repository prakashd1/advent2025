from collections import defaultdict, deque


def parse():
    with open("data/day01.txt", "r") as file:
        return file.readlines()


def part1():
    curr = 50
    r = 0
    for x in inputs:
        x = x.strip()
        direction = x[:1]
        clicks = int(x[1:])
        factor = -1 if direction == "L" else 1
        curr, z = calc(curr, clicks * factor)
        r += (1 if curr == 0 else 0)
        # print(f"{x} Curr {curr} and {(1 if curr == 0 else 0)} {z}")
    print(r)


def part2():
    curr = 50
    r = 0
    for x in inputs:
        x = x.strip()
        direction = x[:1]
        clicks = int(x[1:])
        factor = -1 if direction == "L" else 1
        curr, z = calc(curr, clicks * factor)
        r += (1 if curr == 0 else 0) + z
        # print(f"{x} Curr {curr} and {(1 if curr == 0 else 0)} {z}")
    print(r)


def calc(curr, movement):
    z = 0
    new_pos = (curr + movement) % 100
    if curr == 0 and movement < 0:
        curr = 100

    z += abs((curr + movement) // 100)

    if new_pos == 0 and movement > 0:
        z -= 1

    return new_pos, z

inputs = parse()
part1()
part2()
