# encoding=utf8

"""Implementations of Perm function."""

from niapy.benchmarks.benchmark import Benchmark

__all__ = ['Perm']


class Perm(Benchmark):
    r"""Implementations of Perm functions.

    Date: 2018

    Author: Klemen Berkovič

    License: MIT

    Function:
    **Perm Function**

        :math:`f(\textbf{x}) = \sum_{i = 1}^D \left( \sum_{j = 1}^D (j - \beta) \left( x_j^i - \frac{1}{j^i} \right) \right)^2`

        **Input domain:**
        The function can be defined on any input domain but it is usually
        evaluated on the hypercube :math:`x_i ∈ [-D, D]`, for all :math:`i = 1, 2,..., D`.

        **Global minimum:**
        :math:`f(\textbf{x}^*) = 0` at :math:`\textbf{x}^* = (1, \frac{1}{2}, \cdots , \frac{1}{i} , \cdots , \frac{1}{D})`

    LaTeX formats:
        Inline:
            $f(\textbf{x}) = \sum_{i = 1}^D \left( \sum_{j = 1}^D (j - \beta) \left( x_j^i - \frac{1}{j^i} \right) \right)^2$

        Equation:
            \begin{equation} f(\textbf{x}) = \sum_{i = 1}^D \left( \sum_{j = 1}^D (j - \beta) \left( x_j^i - \frac{1}{j^i} \right) \right)^2 \end{equation}

        Domain:
            $-D \leq x_i \leq D$

    Reference:
        https://www.sfu.ca/~ssurjano/perm0db.html


    """

    Name = ['Perm']

    def __init__(self, dimension=10.0, beta=.5):
        r"""Initialize of Bent Cigar benchmark.

        Args:
            dimension (float): Dimension of the problem.
                -dimension will be the lower bound, dimension will be the upper bound.
            beta (float): Beta parameter.

        See Also:
            :func:`niapy.benchmarks.Benchmark.__init__`

        """
        super().__init__(-dimension, dimension)
        self.beta = beta

    @staticmethod
    def latex_code():
        r"""Return the latex code of the problem.

        Returns:
            str: Latex code.

        """
        return r'''$f(\textbf{x}) = \sum_{i = 1}^D \left( \sum_{j = 1}^D (j - \beta) \left( x_j^i - \frac{1}{j^i} \right) \right)^2$'''

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
            v = .0
            for i in range(1, dimension + 1):
                vv = .0
                for j in range(1, dimension + 1):
                    vv += (j + self.beta) * (x[j - 1] ** i - 1 / j ** i)
                v += vv ** 2
            return v

        return f

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
