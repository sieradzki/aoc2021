with open("input.txt", "r") as f:
    data = f.readlines()
print(len(data))


def get_msb(bit):
    ones_count = 0
    zeros_count = 0
    for line in data:
        if line[bit] == '1':
            ones_count += 1
        elif line[bit] == '0':
            zeros_count += 1
    if ones_count > zeros_count:
        return '1'
    elif ones_count < zeros_count:
        return '0'
    else:
        return '1'


def get_lsb(bit):
    ones_count = 0
    zeros_count = 0
    for line in data:
        if line[bit] == '1':
            ones_count += 1
        elif line[bit] == '0':
            zeros_count += 1
    if ones_count > zeros_count:
        return '0'
    elif ones_count < zeros_count:
        return '1'
    else:
        return '0'


length = len(data[0].strip())

data_copy = []

for line in data:
    data_copy.append(line)
print(len(data_copy))
bit = 0
while len(data) > 1:
    msb = get_msb(bit)

    warden = 0
    while warden == 0:
        for i, line in enumerate(data):
            line = line.strip()
            if line[bit] != msb:
                data.pop(i)
                warden = 0
                break
            warden = 1

    bit += 1

bit = 0
while len(data_copy) > 1:
    lsb = get_lsb(bit)
    if len(data_copy) == 3:
        print('a')
    warden = 0
    while warden == 0:
        for i, line in enumerate(data_copy):
            line = line.strip()
            if line[bit] != lsb:
                data_copy.pop(i)
                warden = 0
                break
            warden = 1

    bit += 1

print(data[0].strip())
print(data_copy[0].strip())

oxygen = int(data[0].strip(), 2)
co2 = int(data_copy[0].strip(), 2)

print(oxygen)
print(co2)

print(oxygen * co2)
