from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import ElementwiseProblem
import numpy as np
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import subprocess
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import FloatRandomSampling
from multiprocessing.pool import ThreadPool
from pymoo.core.problem import StarmapParallelization

class BNH(ElementwiseProblem):

    def __init__(self, **kwargs):
        super().__init__(n_var=2, n_obj=2, n_ieq_constr=2, vtype=float, **kwargs)
        self.xl = np.zeros(self.n_var)
        self.xu = np.array([5.0, 3.0])

    def _evaluate(self, x, out, *args, **kwargs):
        returned = subprocess.check_output(["python3", "BNH_Target.py", str(x[0]), str(x[1])])
        returnedArr = returned.split()
        out["F"] = [float(returnedArr[0]), float(returnedArr[1])]
        out["G"] = [float(returnedArr[2]), float(returnedArr[3])]



algorithm = NSGA2(pop_size=100,
                  sampling=FloatRandomSampling(),
                  crossover=SBX(prob=0.9, eta=15),
                  mutation=PM(eta=20),
                  eliminate_duplicates=True)

n_threads = 32
pool = ThreadPool(n_threads)
runner = StarmapParallelization(pool.starmap)

res = minimize(BNH(elementwise_runner = runner),
               algorithm,
               ('n_gen', 10),
               seed=1,
               verbose=False)
print(f"Threads {n_threads}:", res.exec_time)

Scatter().add(res.F).save("pareto.png")
