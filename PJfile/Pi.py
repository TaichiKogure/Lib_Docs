import numpy as np
import matplotlib.pyplot as plt
import random

# 円周率をモンテカルロ法で近似してみる
m = 0
num = []
pi = []
pi_a = []
for m in range(1, 1000):
    n = 0
    for i in range(m):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x ** 2 + y ** 2 <= 1.0:
            n = n + 1

        pi.append(4.0 * n / m)
        num.append(m)
        pi_a.append(np.pi)
plt.plot(num, pi, label="4*n/m")
plt.plot(num, pi_a, label="pi")

plt.ylim(3,4)

plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

plt.grid(True)

plt.xlabel("number")
plt.ylabel("pi")

plt.legend(loc="upper right")

plt.show()
