from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import Problem
import numpy as np
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import subprocess
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import FloatRandomSampling


class ZDT1(Problem):
    def __init__(self):
        super().__init__(n_var=30, n_obj=2, n_ieq_constr=0, xl=0, xu=1, vtype=float)

    def _evaluate(self, x, out, *args, **kwargs):
        self._run_target_file("target_returnF.npx", "target_returnG.npx", x)
        out["F"] = self._recieve_objective_values("target_returnF.npx", "target_returnG.npx")

    def _run_target_file(self, fileName1: str, fileName2: str, x):
        np.save("population.npy", x)
        subprocess.run(["python3", "targetUsingFile.py", "population.npy", fileName1, fileName2])

    def _recieve_objective_values(self, fileName1: str, fileName2: str):
        with open(fileName1, "rb") as f:
            outF = np.load(f)
        return outF
        

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


Scatter().add(res.F).save("pareto.png")
