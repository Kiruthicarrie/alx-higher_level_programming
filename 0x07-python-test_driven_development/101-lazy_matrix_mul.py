#!/usr/bin/python3
"""Contains definition of lazy_matrix_mul() function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using numpy module

    Args:
        m_a (list): a list of lists containing only integers or floats
            number of columns of m_a must match number of rows of m_b
        m_b (list): a list of lists containing only integers or floats
            number of rows of m_a must match number of columns of m_b

    """

    return np.matmul(m_a, m_b);
