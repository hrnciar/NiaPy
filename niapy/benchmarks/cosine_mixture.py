# encoding=utf8

"""Implementations of Cosine mixture functions."""

import numpy as np
from niapy.benchmarks.benchmark import Benchmark

__all__ = ['CosineMixture']


class CosineMixture(Benchmark):
    r"""Implementations of Cosine mixture function.

    Date: 2018

    Author: Klemen Berkovič

    License: MIT

    Function:
    **Cosine Mixture Function**

        :math:`f(\textbf{x}) = - 0.1 \sum_{i = 1}^D \cos (5 \pi x_i) - \sum_{i = 1}^D x_i^2`

        **Input domain:**
        The function can be defined on any input domain but it is usually
        evaluated on the hypercube :math:`x_i ∈ [-1, 1]`, for all :math:`i = 1, 2,..., D`.

        **Global maximum:**
        :math:`f(x^*) = -0.1 D`, at :math:`x^* = (0.0,...,0.0)`

    LaTeX formats:
        Inline:
            $f(\textbf{x}) = - 0.1 \sum_{i = 1}^D \cos (5 \pi x_i) - \sum_{i = 1}^D x_i^2$

        Equation:
            \begin{equation} f(\textbf{x}) = - 0.1 \sum_{i = 1}^D \cos (5 \pi x_i) - \sum_{i = 1}^D x_i^2 \end{equation}

        Domain:
            $-1 \leq x_i \leq 1$

    Reference:
        http://infinity77.net/global_optimization/test_functions_nd_C.html#go_benchmark.CosineMixture

    """

    Name = ['CosineMixture']

    def __init__(self, lower=-1.0, upper=1.0):
        r"""Initialize of Cosine mixture benchmark.

        Args:
            lower (Optional[float]): Lower bound of problem.
            upper (Optional[float]): Upper bound of problem.

        See Also:
            :func:`niapy.benchmarks.Benchmark.__init__`

        """
        super().__init__(lower, upper)

    @staticmethod
    def latex_code():
        r"""Return the latex code of the problem.

        Returns:
            str: Latex code.

        """
        return r'''$f(\textbf{x}) = - 0.1 \sum_{i = 1}^D \cos (5 \pi x_i) - \sum_{i = 1}^D x_i^2$'''

    def function(self):
        r"""Return benchmark evaluation function.

        Returns:
            Callable[[int, Union[int, float, List[int, float], numpy.ndarray]], float]: Fitness function.

        """
        def f(dimension, x):
            r"""Fitness function.

            Args:
                dimension (int): Dimensionality of the problem
                x (Union[int, float, List[int, float], numpy.ndarray]): Solution to check.

            Returns:
                float: Fitness value for the solution.

            """
            v1, v2 = 0.0, 0.0
            for i in range(dimension):
                v1, v2 = v1 + np.cos(5 * np.pi * x[i]), v2 + x[i] ** 2
            return -0.1 * v1 - v2

        return f

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
