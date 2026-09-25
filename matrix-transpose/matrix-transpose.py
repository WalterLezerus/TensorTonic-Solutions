import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    dimensions = [0,0]
    for x in A:
        dimensions[1] += 1
        if dimensions[1] == 1:
            for y in x:
                dimensions[0] += 1

    output = np.empty((dimensions[0],dimensions[1]))
    
    for x in range(dimensions[1]):
        for y in range(dimensions[0]):
            output[y][x] = A[x][y]
    return output
