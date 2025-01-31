import pandas as pd
import numpy as np

datos= {'Nombre':['Leonardo','Joaquin','Alex','Paula','Enrique', 'Jhon'],
        'Materias':['Lenguaje','EDF','Química','Matemáticas','Inglés','Historia'],
        'Calificaciones':['18','20','13','19','16','17'],
        'Deportes':['Fútbol','Natación','Tenis','Voley','Natación','Balón Mano']
        }
df= pd.DataFrame(datos)
print(df)
print('\n'*4)

#datos no validos
datos2= {'Nombre':['Leonardo','Joaquin','N/A','Paula','Enrique', 'Jhon'],
        'Materias':['Lenguaje','EDF','Química','Matemáticas','Inglés','Historia'],
        'Calificaciones':['18','20',np.nan,'19','16','17'],
        'Deportes':['Fútbol','Natación','Tenis','Voley','N/A','Balón Mano']
        }
df2= pd.DataFrame(datos2)
print(df2)
print('\n'*1)
print(df2.info())

#estadisticas basicas
print(df2.describe())
print('\n'*4)
nuevo= pd.DataFrame(datos2)
nuevo= nuevo.replace(np.nan,"0")
print(nuevo);
#eliminar registro por columnas
columna = df2[~df2['Nombre'].isin(['Joaquin', 'Enrique', 'Jhon'])]
print(columna)

#convertir los numeros a enteros
df['califiaciones']= df.calificaciones.astype(int)
print(df.describe())

#estadistica individuales
print("promedio: ", df['calificaciones'].mean())



