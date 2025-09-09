from sys import argv
import pymoo.gradient.toolbox as anp
import numpy as np


IN_FILE = argv[1]
N_VAR = int(argv[2])


out = {}

with open(IN_FILE, "rb") as f:
    x = np.load(f)

f1 = x[:, 0]

g = 1 + 9.0 / (N_VAR - 1) * anp.sum(x[:, 1:], axis=1)
f2 = g * (1 - anp.power((f1 / g), 0.5))

out["F"] = anp.column_stack([f1, f2])


print(out["F"])
