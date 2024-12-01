input = [[int(x) for x in s.split()] for s in open("2024/inputs/day1").read().split("\n")]

l = []
r = []

for i in input:
    l.append(i[0])
    r.append(i[1])

#Part1
part1 = 0
#Part2
part2 = 0

for x,n in enumerate(sorted(l)):
    part1 += abs(n-sorted(r)[x])
    part2 += n*r.count(n)

print(f"Part: {part1}")
print(f"Part2: {part2}")