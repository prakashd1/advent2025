from collections import defaultdict, deque

def parse():
    with open("data/day01.txt", "r") as file:
        return file.readlines()

def part12():
    curr = 50
    part1, part2 = 0, 0
    for x in inputs:
        direction, clicks = x[:1],  int(x[1:])
        curr, z = calc(curr, clicks * (-1 if direction == "L" else 1))
        part1 += (1 if curr == 0 else 0)
        part2 += (1 if curr == 0 else 0) + z
        # print(f"{x} Curr {curr} and {(1 if curr == 0 else 0)} {z}")
    print(part1)
    print(part2)


def calc(curr, movement):
    z, new_pos = 0 , (curr + movement) % 100
    curr = 100 if (curr == 0 and movement < 0) else curr
    z -= 1 if (new_pos == 0 and movement > 0) else 0
    z += abs((curr + movement) // 100)
    return new_pos, z

inputs = parse()
part12()

