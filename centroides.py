import numpy as np

def genera_centroides(d, clusters):
    """ 
    Genera los centroides de los clusters de manera aleatoria.
    Los centroides se generan de manera uniforme en el rango de valores de cada columna.

    Parámetros:
    -------------
    d : np.array
        datos de entrada
    clusters : int
        número de clusters

    Regresa:
    -------------
    centroides : np.array
        matriz de centroides
    """

    if d.shape[1] < 2:
        raise ValueError('Los datos deben tener al menos 2 dimensiones.')

    min_vals = d.min(axis=0)
    max_vals = d.max(axis=0)
    
    centroides = np.random.uniform(low=min_vals, high=max_vals, size=(clusters, d.shape[1]))
    
    return centroides