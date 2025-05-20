# External library
import numpy as np

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

def masas(lista_masas):
    """Calcular la diagonal y matriz de masa del edificio

    Returns:
        diag_masa: diagonal de matriz de masa (tensor 3)
        col_masa: columna de masas (tensor 2)
    """
    aux_list = []
    diag_matrix = []

    for i in range(len(lista_masas)):
        for j in range(len(lista_masas)):
            if i == j:
                aux_list.append(lista_masas[i])
            else:
                aux_list.append(0)
        
        diag_matrix.append(aux_list)
        aux_list = []   

    return diag_matrix

def factorPartMasas(diag_matrix, modo, lista_masas):
    """Calcular el factor de participación modal

    Args:
        diag_matrix (list): matriz diagonal cuadrada de masas
        modo (list): modo de vibración de los pisos de la estructura
        lista_masas (list): masa de cada piso de la estructura

    Returns:
        float: regresa el valor de la participación modal del modo de vibración
    """
    diag_matrix = np.array(diag_matrix)
    modo = np.array(modo)
    lista_masas = np.array(lista_masas)
    
    f_part_modal = np.dot(modo.T,lista_masas) / np.dot(np.dot(modo,diag_matrix),modo.T)

    return float(f_part_modal)


def fuerzaSismicaCortante(diag_matrix, acc_u):
    """Calculo de la fuerza sísmica y la fuerza cortante

    Args:
        diag_matrix (np.array): matriz de diagonal de masas 
        acc_u (np.array): aceleración por piso para cada modo de vibración

    Returns:
        f_sismica (np.array): fuerza sísmica de cada piso
        f_cortante (np.array): fuerza cortante de cada piso
    """
    f_sismica = np.dot(diag_matrix, acc_u)
    f_cortante = np.zeros(len(acc_u))

    n_pisos = len(acc_u)
    
    for i in range(n_pisos):
        f_cortante[i] = sum(f_sismica[i:n_pisos])

    return f_sismica, f_cortante

def fuerzaSismicaCortanteSumatoria(f_sismicas, f_cortantes):
    n_pisos = len(f_cortantes[0])
    print(n_pisos)
    frcsc = np.zeros(n_pisos)
    #frcsc = np.sqrt(np.sum(np.exp(fuerzaSismicaCortante,2)))
    Vrcsc = np.zeros(n_pisos)

    f_sismicas = np.array(f_sismicas).T
    f_cortantes = np.array(f_cortantes).T

    print(f_sismicas)
    print(f_cortantes)

    for i in range(n_pisos):
        frcsc[i] = (f_sismicas[i][0]**2 + f_sismicas[i][1]**2 + f_sismicas[i][2]**2)**0.5
        Vrcsc[i] = (f_cortantes[i][0]**2 + f_cortantes[i][1]**2 + f_cortantes[i][2]**2)**0.5
    
    return frcsc , Vrcsc

def cortanteRealEstructura(f_sismicas, f_cortantes, R):
    fsum_abs = sum(np.abs(f_sismicas))
    Vsum_abs = sum(np.abs(f_cortantes))

    frcsc, Vrcsc = fuerzaSismicaCortanteSumatoria(f_sismicas, f_cortantes)

    frnc_h = 0.25 * fsum_abs + 0.75 * frcsc #POR COMPLETAR
    Vrnc_h = 0.25 * Vsum_abs + 0.75*Vrcsc

    f_real = frnc_h * 0.75 * R
    V_real = Vrnc_h * 0.75 * R

    return f_real, V_real
