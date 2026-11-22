import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    #for int
    if type(x)==int:
        return 1/(1+ np.exp(-x))

    #for list
    #converting any depth of nested list into numpy array using np.asarray
    x_arr=np.asarray(x, dtype=float) 
    return 1/(1+ np.exp(-x_arr))

        
        