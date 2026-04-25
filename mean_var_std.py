import numpy as np

def calculate(list_values):
    if len(list_values) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list_values).reshape(3, 3)
    
    calculations = {
        'mean': [
            list(np.mean(matrix, axis=0).tolist()),
            list(np.mean(matrix, axis=1).tolist()),
            float(np.mean(matrix))
        ],
        'variance': [
            list(np.var(matrix, axis=0).tolist()),
            list(np.var(matrix, axis=1).tolist()),
            float(np.var(matrix))
        ],
        'standard deviation': [
            list(np.std(matrix, axis=0).tolist()),
            list(np.std(matrix, axis=1).tolist()),
            float(np.std(matrix))
        ],
        'max': [
            list(np.max(matrix, axis=0).tolist()),
            list(np.max(matrix, axis=1).tolist()),
            int(np.max(matrix))
        ],
        'min': [
            list(np.min(matrix, axis=0).tolist()),
            list(np.min(matrix, axis=1).tolist()),
            int(np.min(matrix))
        ],
        'sum': [
            list(np.sum(matrix, axis=0).tolist()),
            list(np.sum(matrix, axis=1).tolist()),
            int(np.sum(matrix))
        ]
    }
    
    return calculations
print(calculate([0,1,2,3,4,5,6,7,8]))