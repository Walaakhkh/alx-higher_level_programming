#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix product.

    Raises:
        ValueError: If the matrices cannot be multiplied.
        TypeError: If m_a or m_b is not a list of lists of integers or floats.
    """
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError as e:
        raise TypeError(str(e))
