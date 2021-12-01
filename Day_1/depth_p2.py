larger = 0

with open("input.txt", "r") as f:
    data = f.readlines()

first_cluster = []
second_cluster = [1, 2, 3]

for i in range(3):
    if data[0].strip() != '':
      first_cluster.append(int(data.pop(0).strip()))

while len(data) >= 1:
  for i in range(2):
    second_cluster[i] = first_cluster[i+1]
  second_cluster[2] = int(data.pop(0).strip())
  if sum(first_cluster) < sum(second_cluster):
    larger += 1

  for i in range(3):
    first_cluster[i] = second_cluster[i]

print(larger)
