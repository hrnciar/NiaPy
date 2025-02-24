# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys

from niapy.algorithms.basic import CovarianceMatrixAdaptionEvolutionStrategy
from niapy.benchmarks import Sphere
from niapy.task import StoppingTask

sys.path.append('../')
# End of fix

# we will run CMA-ES for 5 independent runs
for i in range(5):
    task = StoppingTask(max_evals=1000, enable_logging=True, dimension=10, benchmark=Sphere())
    algo = CovarianceMatrixAdaptionEvolutionStrategy(population_size=20)
    best = algo.run(task)
    print('%s -> %s' % (best[0], best[1]))
