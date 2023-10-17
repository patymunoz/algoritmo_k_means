import numpy as np

def distancia_euclidiana(x, y):
    """
    Calcula la distancia euclidiana entre dos puntos.
    
    Parámetros:
    -------------
    x : np.array
        primer punto
    y : np.array
        segundo punto
    
    Regresa:
    -------------
    distancia : float
        distancia euclidiana entre los dos puntos
    """
    
    distancia = np.sqrt(np.sum((x - y)**2))
    
    return distancia