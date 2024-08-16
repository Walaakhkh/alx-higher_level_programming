#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b.
    
    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.
        
    Returns:
        list of lists: The result of the multiplication.
        
    Raises:
        TypeError: If m_a or m_b is not a list, or if their elements are not lists of integers or floats.
        ValueError: If m_a or m_b is empty, or if they cannot be multiplied.
    """

    # Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate m_a and m_b are not empty
    if not m_a or not all(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not all(m_b):
        raise ValueError("m_b can't be empty")

    # Validate all elements in m_a and m_b are integers or floats
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate that all rows in m_a and m_b are of the same size (rectangular matrices)
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate that the number of columns in m_a equals the number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            element_sum = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row_result.append(element_sum)
        result.append(row_result)
    
    return result
