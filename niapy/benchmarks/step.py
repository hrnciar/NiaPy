# encoding=utf8

"""Implementations of Step functions."""

import math
from niapy.benchmarks.benchmark import Benchmark

__all__ = ['Step', 'Step2', 'Step3']


class Step(Benchmark):
    r"""Implementation of Step function.

    Date: 2018

    Author: Lucija Brezočnik

    License: MIT

    Function: **Step function**

        :math:`f(\mathbf{x}) = \sum_{i=1}^D \left( \lfloor \left |
        x_i \right | \rfloor \right)`

        **Input domain:**
        The function can be defined on any input domain but it is usually
        evaluated on the hypercube :math:`x_i ∈ [-100, 100]`, for all :math:`i = 1, 2,..., D`.

        **Global minimum:** :math:`f(x^*) = 0`, at :math:`x^* = (0,...,0)`

    LaTeX formats:
        Inline:
            $f(\mathbf{x}) = \sum_{i=1}^D \left( \lfloor \left |
            x_i \right | \rfloor \right)$

        Equation:
            \begin{equation} f(\mathbf{x}) = \sum_{i=1}^D \left(
            \lfloor \left | x_i \right | \rfloor \right) \end{equation}

        Domain:
            $-100 \leq x_i \leq 100$

    Reference paper:
        Jamil, M., and Yang, X. S. (2013).
        A literature survey of benchmark functions for global optimisation problems.
        International Journal of Mathematical Modelling and Numerical Optimisation,
        4(2), 150-194.

    """

    Name = ['Step']

    def __init__(self, lower=-100.0, upper=100.0):
        r"""Initialize of Step benchmark.

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
        return r'''$f(\mathbf{x}) = \sum_{i=1}^D \left( \lfloor \left |
                x_i \right | \rfloor \right)$'''

    def function(self):
        r"""Return benchmark evaluation function.

        Returns:
            Callable[[int, Union[int, float, List[int, float], numpy.ndarray]], float]: Fitness function,

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
                val += math.floor(abs(x[i]))

            return val

        return evaluate


class Step2(Benchmark):
    r"""Step2 function implementation.

    Date: 2018

    Author: Lucija Brezočnik

    Licence: MIT

    Function: **Step2 function**

        :math:`f(\mathbf{x}) = \sum_{i=1}^D \left( \lfloor x_i + 0.5 \rfloor \right)^2`

        **Input domain:**
        The function can be defined on any input domain but it is usually
        evaluated on the hypercube :math:`x_i ∈ [-100, 100]`, for all :math:`i = 1, 2,..., D`.

        **Global minimum:** :math:`f(x^*) = 0`, at :math:`x^* = (-0.5,...,-0.5)`

    LaTeX formats:
        Inline:
            $f(\mathbf{x}) = \sum_{i=1}^D \left( \lfloor x_i + 0.5 \rfloor \right)^2$

        Equation:
            \begin{equation}f(\mathbf{x}) = \sum_{i=1}^D \left(
            \lfloor x_i + 0.5 \rfloor \right)^2 \end{equation}

        Domain:
            $-100 \leq x_i \leq 100$

    Reference paper:
        Jamil, M., and Yang, X. S. (2013).
        A literature survey of benchmark functions for global optimisation problems.
        International Journal of Mathematical Modelling and Numerical Optimisation,
        4(2), 150-194.

    """

    Name = ['Step2']

    def __init__(self, lower=-100.0, upper=100.0):
        r"""Initialize of Step2 benchmark.

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
        return r'''$f(\mathbf{x}) = \sum_{i=1}^D \left( \lfloor x_i + 0.5 \rfloor \right)^2$'''

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
                val += math.pow(math.floor(x[i] + 0.5), 2)

            return val

        return evaluate


class Step3(Benchmark):
    r"""Step3 function implementation.

    Date: 2018

    Author: Lucija Brezočnik

    Licence: MIT

    Function: **Step3 function**

        :math:`f(\mathbf{x}) = \sum_{i=1}^D \left( \lfloor x_i^2 \rfloor \right)`

        **Input domain:**
        The function can be defined on any input domain but it is usually
        evaluated on the hypercube :math:`x_i ∈ [-100, 100]`, for all :math:`i = 1, 2,..., D`.

        **Global minimum:** :math:`f(x^*) = 0`, at :math:`x^* = (0,...,0)`

    LaTeX formats:
        Inline:
            $f(\mathbf{x}) = \sum_{i=1}^D \left( \lfloor x_i^2 \rfloor \right)$

        Equation:
            \begin{equation}f(\mathbf{x}) = \sum_{i=1}^D \left(
            \lfloor x_i^2 \rfloor \right)\end{equation}

        Domain:
            $-100 \leq x_i \leq 100$

    Reference paper:
        Jamil, M., and Yang, X. S. (2013).
        A literature survey of benchmark functions for global optimisation problems.
        International Journal of Mathematical Modelling and Numerical Optimisation,
        4(2), 150-194.

    """

    Name = ['Step3']

    def __init__(self, lower=-100.0, upper=100.0):
        r"""Initialize of Step3 benchmark.

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
        return r'''$f(\mathbf{x}) = \sum_{i=1}^D \left( \lfloor x_i^2 \rfloor \right)$'''

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
                val += math.floor(math.pow(x[i], 2))

            return val

        return evaluate
