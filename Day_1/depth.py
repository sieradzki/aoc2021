larger = 0

with open("input.txt", "r") as f:
    data = f.readlines()

prev = int(data.pop(0).strip())

for measurment in data:
    if measurment.strip() != '':
        if prev < int(measurment.strip()):
            larger += 1
        prev = int(measurment.strip())

print(larger)

