with open("input.txt", "r") as f:
    data = f.readlines()

gamma = ""
epsilon = ""

length = len(data[0].strip())

ones_count = [0] * length
zeros_count = [0] * length

for line in data:
    for i, value in enumerate(line.strip()):
        if value == '1':
            ones_count[i] += 1
        elif value == '0':
            zeros_count[i] += 1

# print(f"Ones count: {ones_count}")
# print(f"Zeros count: {zeros_count}")

for i in range(length):
    gamma += '1' if ones_count[i] > zeros_count[i] else '0' 
    epsilon += '0' if ones_count[i] > zeros_count[i] else '1' 
    
print(f"gamma: {gamma}")
print(f"epsilon: {epsilon}")

gamma_10 = int(gamma, 2)
epsilon_10 = int(epsilon, 2)

print(f"gamma_10: {gamma_10}")
print(f"epsilon_10: {epsilon_10}")

power_consumption = gamma_10 * epsilon_10

print(f"power_consumption {power_consumption}")
