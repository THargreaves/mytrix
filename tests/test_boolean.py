"""Tests for Boolean matrices and vectors."""

import unittest

from mytrix.core import BooleanMatrix


class InitialisationTests(unittest.TestCase):
    """Unit test functions related to initialisation."""

    def testZeros(self):
        """Test initialising a matrix of zeros."""
        # Valid initialisation
        m1 = BooleanMatrix.zeros(2, 2)
        self.assertTrue(m1 == BooleanMatrix(2, 2, [
                [False, False],
                [False, False]
            ])
        )
        m2 = BooleanMatrix.zeros(2, 3)
        self.assertTrue(m2 == BooleanMatrix(2, 3, [
                [False, False, False],
                [False, False, False]
            ])
        )

        # Invalid dimensions
        with self.assertRaises(TypeError):
            BooleanMatrix.zeros('spam', 2)
        with self.assertRaises(TypeError):
            BooleanMatrix.zeros(2, 'spam')
        with self.assertRaises(ValueError):
            BooleanMatrix.zeros(0, 2)
        with self.assertRaises(ValueError):
            BooleanMatrix.zeros(2, 0)

    def testOnes(self):
        """Test initialising a matrix of ones."""
        # Valid initialisation
        m1 = BooleanMatrix.ones(2, 2)
        self.assertTrue(m1 == BooleanMatrix(2, 2, [
                [True, True],
                [True, True]
            ])
        )
        m2 = BooleanMatrix.ones(2, 3)
        self.assertTrue(m2 == BooleanMatrix(2, 3, [
                [True, True, True],
                [True, True, True]
            ])
        )

        # Invalid dimensions
        with self.assertRaises(TypeError):
            BooleanMatrix.ones('spam', 2)
        with self.assertRaises(TypeError):
            BooleanMatrix.ones(2, 'spam')
        with self.assertRaises(ValueError):
            BooleanMatrix.ones(0, 2)
        with self.assertRaises(ValueError):
            BooleanMatrix.ones(2, 0)

    def testIdentity(self):
        """Test initialising an identity matrix."""
        # Valid initialisation
        m1 = BooleanMatrix.identity(2)
        self.assertTrue(m1 == BooleanMatrix(2, 2, [
                [True, False],
                [False, True]
            ])
        )

        # Invalid dimensions
        with self.assertRaises(TypeError):
            BooleanMatrix.identity('spam')
        with self.assertRaises(ValueError):
            BooleanMatrix.identity(0)
