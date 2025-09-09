from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import Problem
import numpy as np
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import FloatRandomSampling
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import subprocess
from pymoo.optimize import minimize

import re


class ZDT1(Problem):
    def __init__(self):
        super().__init__(n_var=30, n_obj=2, n_ieq_constr=0, xl=0, xu=1, vtype=float)

    def _evaluate(self, x, out, *args, **kwargs):
        arr = self._run_target_file(x)
        out["F"] = arr

    def _run_target_file(self, x):
        np.save("population.npy", x)
        test = subprocess.check_output(["python3", "targetUsingShellOutput.py", "population.npy", str(self.n_var)])
        decoded = test.decode("utf-8")
        cleaned = re.sub(r"[\[\]]", "", decoded)
        arr = np.fromstring(cleaned, sep=" ")
        arr = arr.reshape(-1, 2)
        return arr

algorithm = NSGA2(pop_size=100,
                  sampling=FloatRandomSampling(),
                  crossover=SBX(prob=0.9, eta=15),
                  mutation=PM(eta=20),
                  eliminate_duplicates=True)

res = minimize(ZDT1(),
               algorithm,
               ('n_gen', 500),
               seed=1,
               verbose=False)

print(res)

Scatter().add(res.F).save("paretoZDT.png")
