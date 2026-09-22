import numpy as np

def dot_product(x: list, y: list) -> float:
    output = 0.0
    for i in range(len(x)):
        output += x[i] * y[i] 
    # Write code here
    return output
    pass