# -*- coding: utf-8 -*-
"""ДЗ 3-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_LRPd__fl5BjU47dj5PXIDn8DRR9ygU_
"""

x = [1, 3, 7]
y = [2, 6, 14]
lr = 0.01
w1 = 0
w0 = 0

for i in range(len(x)):
    prediction = w1 * x[i] + w0
    w1 += 2 * lr * x[i] * (y[i] - prediction)
    w0 += 2 * lr * (y[i] - prediction)

print(w1, w0)

import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.plot(x, [w1 * x + w0 for x in x], color = 'red')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()