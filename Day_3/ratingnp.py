import numpy as np

with open("testinput.txt", "r") as f:
    data = f.readlines()

oxygen_data = np.array(data)
co2_data = np.array(data)

print(oxygen_data)
