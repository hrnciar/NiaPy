# encoding=utf8

"""Implementation of Csendes function."""

import math
from niapy.benchmarks.benchmark import Benchmark

__all__ = ['Csendes']


class Csendes(Benchmark):
    r"""Implementation of Csendes function.

    Date: 2018

    Author: Lucija Brezočnik

    License: MIT

    Function: **Csendes function**

        :math:`f(\mathbf{x}) = \sum_{i=1}^D x_i^6\left( 2 + \sin \frac{1}{x_i}\right)`

        **Input domain:**
        The function can be defined on any input domain but it is usually
        evaluated on the hypercube :math:`x_i ∈ [-1, 1]`, for all :math:`i = 1, 2,..., D`.

        **Global minimum:** :math:`f(x^*) = 0`, at :math:`x^* = (0,...,0)`

    LaTeX formats:
        Inline:
            $f(\mathbf{x}) = \sum_{i=1}^D x_i^6\left( 2 + \sin \frac{1}{x_i}\right)$

        Equation:
            \begin{equation} f(\mathbf{x}) =
            \sum_{i=1}^D x_i^6\left( 2 + \sin \frac{1}{x_i}\right) \end{equation}

        Domain:
            $-1 \leq x_i \leq 1$

    Reference paper:
        Jamil, M., and Yang, X. S. (2013).
        A literature survey of benchmark functions for global optimisation problems.
        International Journal of Mathematical Modelling and Numerical Optimisation,
        4(2), 150-194.

    """

    Name = ['Csendes']

    def __init__(self, lower=-1.0, upper=1.0):
        r"""Initialize of Csendes benchmark.

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
        return r'''$f(\mathbf{x}) = \sum_{i=1}^D x_i^6\left( 2 + \sin \frac{1}{x_i}\right)$'''

    def function(self):
        r"""Return benchmark evaluation function.

        Returns:
            Callable[[int, Union[int, float, List[int, float], numpy.ndarray]], float]: Fitness function.

        """
        def evaluate(dimension, x):
            r"""Fitness function.

            Args:
                dimension (int): Dimensionality of the problem
                x (Union[int, float, List[int, float], numpy.ndarray]): Solution to check.

            Returns:
                float: Fitness value for the solution.

            """
            val = 0.0

            for i in range(dimension):
                if x[i] != 0:
                    val += math.pow(x[i], 6) * (2.0 + math.sin(1.0 / x[i]))

            return val

        return evaluate
