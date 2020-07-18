"""Core components of Mytrix, including matrices and vectors of all types."""

from abc import ABC, abstractmethod


###############
#  MATRICES  #
###############


class Matrix(ABC):
    """A class to represent an abstract general matrix."""

    def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        self.m = m
        self.n = n
        self.data = data

    @property
    @staticmethod
    @abstractmethod
    def _zero():
        """Abstract class property for the zero element of a field."""
        pass

    @property
    @staticmethod
    @abstractmethod
    def _one():
        """Abstract class property for the zero element of a field."""
        pass

    @property
    @staticmethod
    @abstractmethod
    def _type():
        """Abstract class property for the type of matrix elements."""
        pass

    @staticmethod
    def validate_dimensions(m, n):
        """Check whether a pair of matrix dimensions are valid."""
        if not (isinstance(m, int) and isinstance(n, int)):
            raise TypeError("dimensions must be integral")
        if m <= 0 or n <= 0:
            raise ValueError("dimensions must be positive")

    @classmethod
    def from_rows(cls, rows):
        """Make a matrix from a list of rows."""
        m = len(rows)
        n = len(rows[0])
        # Check that rows are consistent lengths
        if any([len(row) != n for row in rows[1:]]):
            raise ValueError("inconsistent row lengths")
        # Dispatch generic function if class is not specified
        if cls is Matrix:
            return Matrix._from_rows_guess_type(m, n, rows)
        # Check that data types match class type
        t = cls._type
        if any(any(type(e) is not t for e in r) for r in rows):
            raise TypeError("element types don't match class type")
        return cls(m, n, rows)

    @staticmethod
    def _from_rows_guess_type(m, n, rows):
        """Make a matrix from a list of rows."""
        # Check that data types are consistent
        t = type(rows[0][0])
        if any(any(type(e) is not t for e in r[(i == 0):])
               for i, r in enumerate(rows)):
            raise TypeError("inconsistent element types")
        # Dispatch to children based on type
        if t is bool:
            return BooleanMatrix(m, n, rows)
        elif t is int:
            return IntegerMatrix(m, n, rows)
        elif t is float:
            return RealMatrix(m, n, rows)
        else:
            raise NotImplementedError(
                "no class implemented for the given element type"
            )

    @classmethod
    def zeros(cls, m, n):
        """Make a matrix of zeros of dimension m by n."""
        Matrix.validate_dimensions(m, n)
        data = [[cls._zero for j in range(n)] for i in range(m)]
        return cls(m, n, data)

    @classmethod
    def ones(cls, m, n):
        """Make a matrix of ones of dimension m by n."""
        Matrix.validate_dimensions(m, n)
        data = [[cls._one if i == j else cls._zero for j in range(n)]
                for i in range(m)]
        return cls(m, m, data)

    @classmethod
    def identity(cls, m):
        """Make an identity matrix of dimension m by m."""
        Matrix.validate_dimensions(m, m)
        data = [[cls._one for j in range(m)] for i in range(m)]
        return cls(m, m, data)


class BooleanMatrix(Matrix):
    """A class to represent a Boolean matrix."""

    _zero = False
    _one = True
    _type = bool


class NumericMatrix(Matrix, ABC):
    """A class to represent a abstract numeric matrix."""

    pass


class IntegerMatrix(NumericMatrix):
    """A class to represent an integer matrix."""

    _zero = 0
    _one = 1
    _type = int


class RationalMatrix(NumericMatrix):
    """A class to represent a rational matrix."""

    def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        raise NotImplementedError(
            "linear algebra over Q is yet to be implemented"
        )


class RealMatrix(NumericMatrix):
    """A class to represent a real matrix."""

    _zero = 0.
    _one = 1.
    _type = float


class ComplexMatrix(NumericMatrix):
    """A class to represent a real matrix."""

    def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        raise NotImplementedError(
            "linear algebra over C is yet to be implemented"
        )


#############
#  VECTORS  #
#############


class Vector(ABC):
    """A class to represent an abstract general vector."""

    def __init__(self, m, data):
        """Initalise vector dimensions and contents."""
        self.m = m
        self.data = data


class BooleanVector(Vector):
    """A class to represent a Boolean vector."""

    pass


class NumericVector(Vector, ABC):
    """A class to represent a abstract numeric vector."""

    pass


class IntegerVector(NumericVector):
    """A class to represent an integer vector."""

    pass


class RationalVector(NumericVector):
    """A class to represent a rational vector."""

    def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        raise NotImplementedError(
            "linear algebra over Q is yet to be implemented"
        )


class RealVector(NumericVector):
    """A class to represent a real vector."""

    pass


class ComplexVector(NumericVector):
    """A class to represent a real vector."""

    def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        raise NotImplementedError(
            "linear algebra over C is yet to be implemented"
        )
