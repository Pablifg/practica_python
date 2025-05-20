import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sb
from math import sin, cos, pi, sqrt

import seismicAnalysis as sa




def main(*args):
    factoresC = []
    pseudo_aceleracion = []
    freq_str = [] # frecuencia estructural
    desp_espectral = []
    f_part_modal = []
    f_sismicas = [] # fuerzas sísmicas
    f_cortantes = [] # fuerzas cortantes

    counter=1

    for t in periodos:
        C = sa.C(T=t, Tp=0.4, Tl=2.5)
        print(C)
        factoresC.append(C)
        
        Sa=Z*U*C*S/R*g # m/s2
        pseudo_aceleracion.append(Sa)

        w = 2* pi / t # s
        freq_str.append(w)

        sd = Sa / w**2 # desplazamiento espectral. m
        desp_espectral.append(sd)

        diag_matrix = sa.masas(lista_masas)

        fpm = sa.factorPartMasas(diag_matrix, datos_edificio["modo"+str(counter)],lista_masas)
        f_part_modal.append(fpm)

        acc_u = Sa * fpm * np.array(datos_edificio["modo"+str(counter)])
        
        f_sismica, f_cortante = sa.fuerzaSismicaCortante(diag_matrix, acc_u)

        f_sismicas.append(f_sismica)
        f_cortantes.append(f_cortante)

        

        counter = counter+1

    print(f_sismicas)

    f_real, V_real = sa.cortanteRealEstructura(f_sismicas, f_cortantes, R)

    print(periodos)
    print(factoresC)
    print(pseudo_aceleracion)
    print(freq_str)
    print(desp_espectral)
    print(diag_matrix)
    print(f_part_modal)
    print(acc_u)
    print(f_sismica)
    print(f_cortante)
    print("LAS FUERZAS REALES SON: ")
    print(f_real)
    print("EL CORTANTE REAL ES DE: ")
    print(V_real)

if __name__ == "__main__":
    
    # Datos
    H=3     # altura del edificio (s)
    S=1.0   
    Z=0.45  # factor de zona sismica
    Tp=0.4  # Periodo corto (s)
    Tl =2.5 # Periodo largo (s)
    U=1.0   # Factor de importancia
    Ct=35   # Coeficiente oara edificios aporticadas (m/s)
    periodos = [0.556, 0.193, 0.126]
    # Cálculos
    T=5*H/Ct # Periodo de vibración de la estructura (s)
    Ia = 1.0
    Ip=1.0
    Ro=8
    R=Ia * Ip * Ro
    g = 9.81 # aceleraciòn de gravedad (m/s2)
    lista_masas=[31.80, 31.80, 31.80, 31.80, 27.50]

    datos_edificio = {
        "pisos": [1,2,3,4,5],
        "modo1": [0.03112, 0.05959, 0.08302, 0.09940, 0.10834],
        "modo2": [-0.08102, -0.10193, -0.05484, 0.03358, 0.10609],
        "modo3": [0.10415, 0.03021, -0.09525, -0.05769, 0.09176]
    }
    
    main(H,S,Z,Tp,Tl,U,Ct,periodos,T,Ia,Ip,R,g, lista_masas, datos_edificio)