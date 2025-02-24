# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys

sys.path.append('../')
# End of fix

from niapy.task import StoppingTask
from niapy.benchmarks import Sphere
from niapy.algorithms.basic import CatSwarmOptimization

task = StoppingTask(max_evals=1000, enable_logging=True, dimension=10, benchmark=Sphere())
algo = CatSwarmOptimization()
best = algo.run(task=task)
print('%s -> %s' % (best[0], best[1]))
# plot a convergence graph
task.plot()
