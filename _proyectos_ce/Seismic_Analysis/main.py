import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sb


import seismicAnalysis as sa




def main(periodos):
    factoresC = []
    for t in periodos:
        C = sa.C(T=t, Tp=0.4, Tl=2.5)
        print(C)
        factoresC.append(C)
    print(factoresC)

if __name__ == "__main__":
    
    # Datos
    H=3     # altura del edificio (s)
    S=1.0   # factor de zona sismica
    Tp=0.4  # Periodo corto (s)
    Tl =2.5 # Periodo largo (s)
    U=1.0   # Factor de importancia
    Ct=35   # Coeficiente oara edificios aporticadas (m/s)
    periodos = [0.556, 0.193, 0.126]
    # Cálculos
    T=5*H/Ct # Periodo de vibración de la estructura (s)
    main(periodos)