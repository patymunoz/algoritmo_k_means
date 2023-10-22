import numpy as np

from centroides import genera_centroides
from distancia import distancia_euclidiana

def kmeans(d, k):
    """ 
    Agrupa los datos de entrada de acuerdo con el número de clusters especificado.

    Parámetros:
    -------------
    d : np.array
        datos de entrada
    k : int
        número de clusters

    Regresa:
    -------------
    etiquetas : np.array
        etiquetas asignadas a cada punto
    n_centroides : np.array
        posiciones de los centroides de los clusters
    """
    array_centroides = genera_centroides(d, k)
    n_centroides = np.copy(array_centroides)

    dicc_centroides = {}

    while True:
        distancias = np.array([[distancia_euclidiana(fila, centroide) for centroide in array_centroides] for fila in d])
        etiquetas = np.argmin(distancias, axis=1)
        n_centroides = np.array([d[etiquetas == i].mean(axis=0) for i in range(k)])

        # criterio de convergencia
        if np.all(array_centroides == n_centroides):
            break

        array_centroides = np.copy(n_centroides)
        dicc_centroides[f'iteracion_{len(dicc_centroides) + 1}'] = array_centroides

    return etiquetas, n_centroides, dicc_centroides