import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    arr_x = np.asarray(x, dtype=float)
    return np.maximum(0, arr_x)