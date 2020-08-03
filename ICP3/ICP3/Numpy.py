import numpy as np

b = np.random.randint(low=1, high=20, size=15)

print(b)

result = np.where(b == np.amax(b))

for index in result[0]:
    b[index] = 0

print(b)
