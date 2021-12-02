with open("input.txt", "r") as f:
    data = f.readlines()

horizontal = 0
depth = 0
aim = 0

for line in data:
    line = line.strip()
    if line.find("forward") != -1:
        horizontal += int(line[-1])
        depth += aim * int(line[-1])
    elif line.find("down") != -1:
        aim += int(line[-1])
    elif line.find("up") != -1:
        aim -= int(line[-1])

print(f"Horizontal: {horizontal}")
print(f"Depth: {depth}")
print(f"Aim: {aim}")

final = horizontal * depth

print(f"Final: {final}")
