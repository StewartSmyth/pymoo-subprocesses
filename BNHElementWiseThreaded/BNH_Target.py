from sys import argv
import pymoo.gradient.toolbox as anp

x = []

x.append(float(argv[1]))
x.append(float(argv[2]))


f1 = 4 * x[0] ** 2 + 4 * x[1] ** 2
f2 = (x[0] - 5) ** 2 + (x[1] - 5) ** 2
g1 = (1 / 25) * ((x[0] - 5) ** 2 + x[1] ** 2 - 25)
g2 = -1 / 7.7 * ((x[0] - 8) ** 2 + (x[1] + 3) ** 2 - 7.7)

print(f1, f2, g1, g2)

