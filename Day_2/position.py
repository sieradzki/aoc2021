with open("input.txt", "r") as f:
    data = f.readlines()

horizontal = 0
depth = 0

for line in data:
    line = line.strip()
    if line.find("forward") != -1:
        horizontal += int(line[-1])
    elif line.find("down") != -1:
        depth += int(line[-1])
    elif line.find("up") != -1:
        depth -= int(line[-1])

print(f"Horizontal: {horizontal}")
print(f"Depth: {depth}")

final = horizontal * depth

print(f"Final: {final}")
