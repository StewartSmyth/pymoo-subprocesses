from sys import argv
import numpy as np
import pymoo.gradient.toolbox as anp


POPFILE = argv[1]
OUTFILE1 = argv[2]
OUTFILE2 = argv[3]
N_VAR = 30

with open(POPFILE, "rb") as f:
    x = np.load(f)

out = {}

f1 = x[:, 0]

g = 1 + 9.0 / (N_VAR - 1) * anp.sum(x[:, 1:], axis=1)
f2 = g * (1 - anp.power((f1 / g), 0.5))

out["F"] = anp.column_stack([f1, f2])


with open(OUTFILE1, "wb") as f:
    np.save(f, out["F"])

