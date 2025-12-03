from collections import defaultdict, deque
import re
def parse():
    with open("./data/day03.txt", "r") as file:
        content = file.readlines()
    return content


def part12(c):
    r1, r2 = 0 , 0
    for x in c:
        x = x.strip()
        r1 += int(find_joltage(x, 2))
        r2 += int(find_joltage(x, 12))
    print(r1, r2)

def find_joltage(line, k):
    if len(line) < k:
        return 0
    d, r = re.findall(r'\d', line), []
    for i in range(k):
        dr = k - i
        end = len(d) - dr + 1
        bd = max(d[:end])
        bdi = d[:end].index(bd)
        r.append(bd)
        d = d[bdi+1:]
    #print(f"for {line} joltage is {"".join(r)}")
    return "".join(r)

c = parse()
part12(c)