# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys

sys.path.append('../')
# End of fix

from niapy.algorithms.modified import DifferentialEvolutionMTSv1
from niapy.algorithms.basic.de import cross_best2
from niapy.task import StoppingTask
from niapy.benchmarks import Sphere

# we will run Differential Evolution for 5 independent runs
for i in range(5):
    task = StoppingTask(max_evals=10000, dimension=10, benchmark=Sphere())
    algo = DifferentialEvolutionMTSv1(population_size=50, differential_weight=0.5, crossover_probability=0.9, strategy=cross_best2, num_tests=5, num_searches=3,
                                      num_enabled=4)
    best = algo.run(task)
    print('%s -> %s' % (best[0], best[1]))
