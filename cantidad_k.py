import numpy as np

from distancia import distancia_euclidiana

def calcular_wcss(d, etiquetas, centroides):
    """
    Calcula la suma de las distancias cuadradas dentro de los clusters (WCSS).

    Parámetros:
    -------------
    d : np.array
        datos de entrada
    etiquetas : np.array
        etiquetas asignadas a cada punto
    centroides : np.array
        posiciones de los centroides de los clusters

    Regresa:
    -------------
    wcss : float
        suma de las distancias cuadradas dentro de los clusters
    """
    
    wcss = sum([distancia_euclidiana(d[i], centroides[etiquetas[i]])**2 for i in range(len(d))])
    return wcss
