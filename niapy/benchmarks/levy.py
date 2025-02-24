# encoding=utf8

"""Implementations of Levy function."""

import numpy as np
from niapy.benchmarks.benchmark import Benchmark

__all__ = ['Levy']


class Levy(Benchmark):
    r"""Implementations of Levy functions.

    Date: 2018

    Author: Klemen Berkovič

    License: MIT

    Function:
    **Levy Function**

        :math:`f(\textbf{x}) = \sin^2 (\pi w_1) + \sum_{i = 1}^{D - 1} (w_i - 1)^2 \left( 1 + 10 \sin^2 (\pi w_i + 1) \right) + (w_d - 1)^2 (1 + \sin^2 (2 \pi w_d)) \\ w_i = 1 + \frac{x_i - 1}{4}`

        **Input domain:**
        The function can be defined on any input domain but it is usually
        evaluated on the hypercube :math:`x_i ∈ [-10, 10]`, for all :math:`i = 1, 2,..., D`.

        **Global minimum:**
        :math:`f(\textbf{x}^*) = 0` at :math:`\textbf{x}^* = (1, \cdots, 1)`

    LaTeX formats:
        Inline:
            $f(\textbf{x}) = \sin^2 (\pi w_1) + \sum_{i = 1}^{D - 1} (w_i - 1)^2 \left( 1 + 10 \sin^2 (\pi w_i + 1) \right) + (w_d - 1)^2 (1 + \sin^2 (2 \pi w_d)) \\ w_i = 1 + \frac{x_i - 1}{4}$

        Equation:
            \begin{equation} f(\textbf{x}) = \sin^2 (\pi w_1) + \sum_{i = 1}^{D - 1} (w_i - 1)^2 \left( 1 + 10 \sin^2 (\pi w_i + 1) \right) + (w_d - 1)^2 (1 + \sin^2 (2 \pi w_d)) \\ w_i = 1 + \frac{x_i - 1}{4} \end{equation}

        Domain:
            $-10 \leq x_i \leq 10$

    Reference:
        https://www.sfu.ca/~ssurjano/levy.html

    """

    Name = ['Levy']

    def __init__(self, lower=0.0, upper=np.pi):
        r"""Initialize of Levy benchmark.

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
        return r'''$f(\textbf{x}) = \sin^2 (\pi w_1) + \sum_{i = 1}^{D - 1} (w_i - 1)^2 \left( 1 + 10 \sin^2 (\pi w_i + 1) \right) + (w_d - 1)^2 (1 + \sin^2 (2 \pi w_d)) \\ w_i = 1 + \frac{x_i - 1}{4}$'''

    def function(self):
        r"""Return benchmark evaluation function.

        Returns:
            Callable[[int, Union[int, float, List[int, float], numpy.ndarray]], float]: Fitness function.

        """
        def w(x):
            return 1 + (x - 1) / 4

        def f(dimension, x):
            r"""Fitness function.

            Args:
                dimension (int): Dimensionality of the problem
                x (Union[int, float, List[int, float], numpy.ndarray]): Solution to check.

            Returns:
                float: Fitness value for the solution.

            """
            v = 0.0
            for i in range(dimension - 1):
                v += (w(x[i]) - 1) ** 2 * (1 + 10 * np.sin(np.pi * w(x[i]) + 1) ** 2) + (w(x[-1]) - 1) ** 2 * (1 + np.sin(2 * np.pi * w(x[-1]) ** 2))
            return np.sin(np.pi * w(x[0])) ** 2 + v

        return f

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
