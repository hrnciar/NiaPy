# encoding=utf8

"""Implementations of Dixon Price function."""

from niapy.benchmarks.benchmark import Benchmark

__all__ = ['DixonPrice']


class DixonPrice(Benchmark):
    r"""Implementations of Dixon Price function.

    Date: 2018

    Author: Klemen Berkovič

    License: MIT

    Function:
    **Dixon Price Function**

        :math:`f(\textbf{x}) = (x_1 - 1)^2 + \sum_{i = 2}^D i (2x_i^2 - x_{i - 1})^2`

        **Input domain:**
        The function can be defined on any input domain but it is usually
        evaluated on the hypercube :math:`x_i ∈ [-10, 10]`, for all :math:`i = 1, 2,..., D`.

        **Global minimum:**
        :math:`f(\textbf{x}^*) = 0` at :math:`\textbf{x}^* = (2^{-\frac{2^1 - 2}{2^1}}, \cdots , 2^{-\frac{2^i - 2}{2^i}} , \cdots , 2^{-\frac{2^D - 2}{2^D}})`

    LaTeX formats:
        Inline:
            $f(\textbf{x}) = (x_1 - 1)^2 + \sum_{i = 2}^D i (2x_i^2 - x_{i - 1})^2$

        Equation:
            \begin{equation} f(\textbf{x}) = (x_1 - 1)^2 + \sum_{i = 2}^D i (2x_i^2 - x_{i - 1})^2 \end{equation}

        Domain:
            $-10 \leq x_i \leq 10$

    Reference:
        https://www.sfu.ca/~ssurjano/dixonpr.html

    """

    Name = ['DixonPrice']

    def __init__(self, lower=-10.0, upper=10):
        r"""Initialize of Dixon Price benchmark.

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
        return r'''$f(\textbf{x}) = (x_1 - 1)^2 + \sum_{i = 2}^D i (2x_i^2 - x_{i - 1})^2$'''

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
            v = 0.0
            for i in range(2, dimension):
                v += i * (2 * x[i] ** 2 - x[i - 1]) ** 2
            return (x[0] - 1) ** 2 + v

        return f

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
