# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 07:55:30 2025

@author: usuario
"""

import pandas as pd
import numpy as np
datos= pd.read_csv('living.csv')
print(datos.head())
print(datos.info())

print("\n"*4)

print(datos.iloc[0:5])
print(datos.iloc[0:21:2])
print(datos.iloc[[0,3,6,24],])
#columnas
#print(datos.iloc[:,0:2])

print(datos.iloc[[0,3,6,24],[0,2,3]])