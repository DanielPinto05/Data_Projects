from matplotlib import pyplot as plt
import numpy as np
import random

# Goal: Use np.linspace to make calculus functions.

n = 101
max = 50
x = list(np.linspace(0, max, num=n))
y = list(np.linspace(0, max, num=n))
z = []


for i in range(len(y)):
    y[i] = 4 * (y[i] ** 4) - 3 * (y[i] ** 3) - 5 * (y[i] ** 2) + 7


print(y)

for i in range(n):  # making some cool random data\
    z.append(random.randint(0, max**2))


plt.close()
plt.scatter(x, y, color="orange", s=20, label="Good data")
plt.scatter(x, z, color="blue", s=20, label="Random data")


plt.grid()
plt.title("Quick Demonstration")
plt.xlabel("x [mm^4/W]")
plt.ylabel("y lb_f")
plt.legend()
plt.show()
