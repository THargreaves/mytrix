"""Core components of Mytrix, including matrices and vectors of all types."""

from abc import ABC, abstractmethod

import mytrix.expections as exc

################
##  MATRICES  ##
################

class Matrix(ABC):
	"""A class to represent an abstract general matrix."""

    def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        self.m = m
        self.n = n
        self.data = data


class BooleanMatrix(Matrix):
	"""A class to represent a Boolean matrix."""
	pass


class NumericMatrix(Matrix, ABC):
	"""A class to represent a abstract numeric matrix."""
	pass


class IntegerMatrix(Matrix):
	"""A class to represent an integer matrix."""
	pass


class RationalMatrix(Matrix):
	"""A class to represent a rational matrix."""
	
	def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        raise NotImplementedError(
        	"linear algebra over Q is yet to be implemented"
        )


class RealMatrix(Matrix):
	"""A class to represent a real matrix."""
	pass


class ComplexMatrix(Matrix):
	"""A class to represent a real matrix."""
	
	def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        raise NotImplementedError(
        	"linear algebra over C is yet to be implemented"
        )

###############
##  VECTORS  ##
###############

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


class IntegerVector(Vector):
	"""A class to represent an integer vector."""
	pass


class RationalVector(Vector):
	"""A class to represent a rational vector."""
	
	def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        raise NotImplementedError(
        	"linear algebra over Q is yet to be implemented"
        )


class RealVector(Vector):
	"""A class to represent a real vector."""
	pass


class ComplexVector(Vector):
	"""A class to represent a real vector."""
	
	def __init__(self, m, n, data):
        """Initalise matrix dimensions and contents."""
        raise NotImplementedError(
        	"linear algebra over C is yet to be implemented"
        )
