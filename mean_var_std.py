import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)

    mean = [
        np.mean(matrix, axis=0).tolist(),
        np.mean(matrix, axis=1).tolist(),
        np.mean(matrix).item()
    ]

    variance = [
        np.var(matrix, axis=0).tolist(),
        np.var(matrix, axis=1).tolist(),
        np.var(matrix).item()
    ]

    standard_deviation = [
        np.std(matrix, axis=0).tolist(),
        np.std(matrix, axis=1).tolist(),
        np.std(matrix).item()
    ]

    max_value = [
        np.max(matrix, axis=0).tolist(),
        np.max(matrix, axis=1).tolist(),
        np.max(matrix).item()
    ]

    min_value = [
        np.min(matrix, axis=0).tolist(),
        np.min(matrix, axis=1).tolist(),
        np.min(matrix).item()
    ]

    sum_value = [
        np.sum(matrix, axis=0).tolist(),
        np.sum(matrix, axis=1).tolist(),
        np.sum(matrix).item()
    ]

    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }
