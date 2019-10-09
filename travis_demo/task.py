import numpy as np


def sum_plus_one(x1, x2):
    """Adds to arrays then adds one to each element

    Paramaters
    ----------

    x1, x2 : array_like
        The arrays to be added and have 1 added to their elements

    
    Returns
    -------
    ndarray or scalar
        The sum of x1 and x2, element-wise plus 1 to each entry. This
        is a scalar if both x1 and x2 are scalars.

    """
    return np.add(x1, x2) + 1

