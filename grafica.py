import plotly.graph_objects as go
import numpy as np

def plot_kmeans(d, etiquetas, dicc_centroides, i_centroides=True, f_centroides=True):
    """ 
    Grafica los clústers y los centroides iniciales y finales.

    Parámetros:
    -------------
    d : np.array
        datos de entrada
    etiquetas : np.array
        etiquetas asignadas a cada punto
    dicc_centroides : dict
        diccionario con los centroides de cada iteración
    i_centroides : bool
        indica si se grafican los centroides iniciales
    f_centroides : bool
        indica si se grafican los centroides finales
    
    Regresa:
    -------------
    Gráfica de los clústers y los centroides (si se especifica).
    """
    fig = go.Figure()
    colores_clusters = ['blue', 'purple', 'orange', 'red', 'green']

    dimensiones = d.shape[1]

    if dimensiones == 2:
        # Agrega los datos coloreados por etiqueta
        for i in range(len(np.unique(etiquetas))):
            idx = np.where(etiquetas == i)
            fig.add_trace(go.Scatter(x=d[idx, 0][0], y=d[idx, 1][0], mode='markers', 
                                     marker=dict(color=colores_clusters[i]), 
                                     name=f'Cluster {i+1}'))

        if i_centroides:          
            i_centroides = dicc_centroides['iteracion_1']

            fig.add_trace(go.Scatter(x=i_centroides[:, 0], y=i_centroides[:, 1], mode='markers',
                                     marker=dict(symbol='circle', size=10, color='black', line=dict(width=2)),
                                     name='Centroides Iniciales'))

        if f_centroides:
            f_centroides = dicc_centroides[f'iteracion_{len(dicc_centroides)}']
            
            fig.add_trace(go.Scatter(x=f_centroides[:, 0], y=f_centroides[:, 1], mode='markers',
                                 marker=dict(symbol='x', size=10, color='green', line=dict(width=2)),
                                 name='Centroides Finales'))

        # Configuración y mostrar gráfica
        fig.update_layout(title="K-Means", xaxis_title="X", yaxis_title="Y")
        fig.show()

    elif dimensiones == 3:
        for i in range(len(np.unique(etiquetas))):
            idx = np.where(etiquetas == i)
            fig.add_trace(go.Scatter3d(x=d[idx, 0][0], y=d[idx, 1][0], z=d[idx, 2][0], mode='markers',
                                       marker=dict(color=colores_clusters[i]), 
                                       name=f'Cluster {i+1}'))

        if i_centroides:          
            i_centroides = dicc_centroides['iteracion_1']

            fig.add_trace(go.Scatter(x=i_centroides[:, 0], y=i_centroides[:, 1], mode='markers',
                                     marker=dict(symbol='circle', size=10, color='black', line=dict(width=2)),
                                     name='Centroides Iniciales'))

        if f_centroides:
            f_centroides = dicc_centroides[f'iteracion_{len(dicc_centroides)}']
            
            fig.add_trace(go.Scatter(x=f_centroides[:, 0], y=f_centroides[:, 1], mode='markers',
                                 marker=dict(symbol='x', size=10, color='green', line=dict(width=2)),
                                 name='Centroides Finales'))

        # Configuración y mostrar gráfica
        fig.update_layout(title="Centroides Iniciales y Finales en K-Means 3D")
        fig.show()

    else:
        print("No es posible graficar datos con más de 3 dimensiones.")