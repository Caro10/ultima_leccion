#analisis de datos

#importante los indices
''''
skiprows no queir algunas filas especificas

#crear un archivo, csv  con excel, a pie
con informacion como  compras.csv

frutas 10000

carnes 10000

verduras 5000

lacteos 10 000

usar jupyter

crear un datafreme con nombres de columnas  'producto' 'precio'


pd.read_csv('examples/ex2.csv', names=['a','b','c','d', 'message']) para poner nombre

calcular total de todas las compras
calcular el promedio

en jupyter:

import pandas as pd

df = pd.read_csv('Compras.csv', names=['producto','precio'])

df['precio'].sum()

df['precio'].mean()

Expresiones regulares:

