import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    numerator = np.dot(a,b)
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    if numerator == 0 or denominator == 0:
        return 0.0
    output = numerator / denominator

    return float(output)
    pass