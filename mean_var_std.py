import numpy as np
def valores(array, axi = None):
    mid = np.mean(array, axis=axi)
    var = np.var(array, axis=axi)
    std = np.std(array, axis=axi)
    max = np.max(array, axis=axi)
    min = np.min(array, axis=axi)
    sum = np.sum(array, axis=axi)
    return mid, var, std, max, min, sum

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    try:
        lista = np.array(lst)
        reshapeList = lista.reshape((3,3))
        media, varianza, standard_deviation, maximo, minimo, suma = valores(reshapeList)
        media0, varianza0, standard_deviation0, maximo0, minimo0, suma0 = valores(reshapeList, 0)
        media1, varianza1, standard_deviation1, maximo1, minimo1, suma1 = valores(reshapeList, 1)

        calculations = {
            'mean': [media0.tolist(), media1.tolist(), media],
            'variance': [varianza0.tolist(), varianza1.tolist(), varianza],
            'standard deviation': [standard_deviation0.tolist(), standard_deviation1.tolist(), standard_deviation],
            'max': [maximo0.tolist(),maximo1.tolist(), maximo],
            'min': [minimo0.tolist(), minimo1.tolist(), minimo],
            'sum': [suma0.tolist(), suma1.tolist(), suma]
        }
        return calculations
    except Exception as error:
        return str(error)
