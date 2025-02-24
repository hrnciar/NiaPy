# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys

sys.path.append('../')
# End of fix

from niapy.algorithms.basic import SineCosineAlgorithm
from niapy.task import StoppingTask
from niapy.benchmarks import Sphere

# we will run Sine Cosine Algorithm algorithm for 5 independent runs
for i in range(5):
    task = StoppingTask(max_evals=10000, dimension=10, benchmark=Sphere())
    algo = SineCosineAlgorithm(population_size=30, a=7, r_min=0.1, r_max=3)
    best = algo.run(task=task)
    print(best)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
