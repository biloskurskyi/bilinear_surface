import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from tkinter.colorchooser import askcolor
import numpy as np

# Q(u, w) = P(0,0)(1-u)(1-w) + P(0,1)(1-u)(w) + P(1,0)(u)(1-w) + P(1,1)(u)(w)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = [0, 0, 0]

P00 = np.array([0, 0, 1])
P01 = np.array([1, 1, 1])
P10 = np.array([1, 0, 1])
P11 = np.array([0, 1, 0])

Quw = []

"""P00_x = float(input("Введіть координату X для P00: "))
P00_y = float(input("Введіть координату Y для P00: "))
P00_z = float(input("Введіть координату Z для P00: "))
P00 = np.array([P00_x, P00_y, P00_z])

P01_x = float(input("Введіть координату X для P01: "))
P01_y = float(input("Введіть координату Y для P01: "))
P01_z = float(input("Введіть координату Z для P01: "))
P01 = np.array([P01_x, P01_y, P01_z])

P10_x = float(input("Введіть координату X для P10: "))
P10_y = float(input("Введіть координату Y для P10: "))
P10_z = float(input("Введіть координату Z для P10: "))
P10 = np.array([P10_x, P10_y, P10_z])

P11_x = float(input("Введіть координату X для P11: "))
P11_y = float(input("Введіть координату Y для P11: "))
P11_z = float(input("Введіть координату Z для P11: "))
P11 = np.array([P11_x, P11_y, P11_z])"""

max1 = P00[0]
if P01[0] > max1:
    max1 = P01[0]
if P10[0] > max1:
    max1 = P10[0]
if P11[0] > max1:
    max1 = P11[0]

max2 = P00[1]
if P01[1] > max2:
    max2 = P01[1]
if P10[1] > max2:
    max2 = P10[1]
if P11[1] > max2:
    max2 = P11[1]

max3 = P00[2]
if P01[2] > max3:
    max3 = P01[2]
if P10[2] > max3:
    max3 = P10[2]
if P11[2] > max3:
    max3 = P11[2]

"""print(max1)
print(max2)
print(max3)"""

endpoints = [
    [max1, 0, 0],
    [0, max2, 0],
    [0, 0, max3],
]

print("P00 =", P00)
print("P01 =", P01)
print("P10 =", P10)
print("P11 =", P11)

for endpoint, color, label in zip(endpoints, ['r', 'g', 'b'], ['X', 'Y', 'Z']):
    ax.quiver(*origin, *endpoint, color=color, label=label)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim([0, max1])
ax.set_ylim([0, max2])
ax.set_zlim([0, max3])

# u = 0.5
# w = 0.5
i = 0

n = 1 / 0.1

Quw = np.zeros((int(n + 1), int(n + 1), 3))

for i in range(int(n + 1)):
    u = i * 0.1
    for j in range(int(n + 1)):
        w = j * 0.1
        result = P00 * (1 - u) * (1 - w) + P01 * (1 - u) * w + P10 * u * (1 - w) + P11 * u * w
        Quw[i, j, :] = result

ax.scatter(P00[0], P00[1], P00[2], color='red', marker='o', label='P00')
ax.scatter(P01[0], P01[1], P01[2], color='green', marker='o', label='P01')
ax.scatter(P10[0], P10[1], P10[2], color='blue', marker='o', label='P10')
ax.scatter(P11[0], P11[1], P11[2], color='purple', marker='o', label='P11')

line = input("Виберіть стиль лінії для розмітки(1 = -, 2 = -., 3 = :, Будь яке інше значення = --): ")
if line == '1':
    line = '-'
elif line == '2':
    line = '-.'
elif line == '3':
    line = ':'
else:
    line = '--'

for i in range(int(n)):
    for j in range(int(n)):
        ax.plot([Quw[i, j, 0], Quw[i, j + 1, 0], Quw[i + 1, j + 1, 0], Quw[i + 1, j, 0], Quw[i, j, 0]],
                [Quw[i, j, 1], Quw[i, j + 1, 1], Quw[i + 1, j + 1, 1], Quw[i + 1, j, 1], Quw[i, j, 1]],
                [Quw[i, j, 2], Quw[i, j + 1, 2], Quw[i + 1, j + 1, 2], Quw[i + 1, j, 2], Quw[i, j, 2]],
                color='gray', linestyle=line)


vertices = [Quw[0, 0], Quw[0, -1], Quw[-1, -1], Quw[-1, 0]]


def choose_color():
    color = askcolor()[1]
    if color:
        return color
    return 'pink'


print("Чи не хотіли б ви обрати колір для замалювання площини?")
print("Тоді введіть: \"Так\"!")
yes = input("Поле для вводу: ")
if yes == "Так":
    color = choose_color()
    poly = [vertices]
    ax.add_collection3d(Poly3DCollection(poly, alpha=0.5, facecolors=color, edgecolors='k'))

plt.legend()
plt.show()
