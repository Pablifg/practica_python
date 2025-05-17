def C(T=None, Tp=None, Tl=None):
    """Calcula el factor de amplificación sísmica (C).
    
    Returns:
    T: (float) periodo de la estructura en segundos
    Tp: (float) en segundos
    Tl: (float) en segundos
    """

    if (T < Tp):
        return 2.5
    elif (T < Tl):
        return 2.5 * (Tp / T)
    
    return 2.5 * ((Tp * Tl) / T**2)

def masas():
    """Calcular la diagonal y matriz de masa del edificio

    Returns:
        diag_masa: diagonal de matriz de masa (tensor 3)
        col_masa: columna de masas (tensor 2)
    """
    diag = 0
    matrix = 0 
    return diag, matrix