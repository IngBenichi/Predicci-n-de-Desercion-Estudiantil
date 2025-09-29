import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Número de registros
n = 500

# Generar variables demográficas
edad = np.random.randint(17, 26, size=n)  # 17 a 25 años
genero = np.random.choice(['M', 'F'], size=n)
lugar_origen = [fake.city() for _ in range(n)]

# Variables académicas
promedio_colegio = np.round(np.random.uniform(3.0, 5.0, size=n), 2)  # 0-5
admission_test = np.random.randint(50, 100, size=n)  # 50-100
primer_semestre = np.round(np.random.uniform(2.0, 5.0, size=n), 2)  # 0-5

# Variables financieras
nivel_socioeconomico = np.random.choice(['Bajo', 'Medio', 'Alto'], size=n)
beca = np.random.choice([0, 1], size=n)  # 0=no, 1=si
prestamo = np.random.choice([0, 1], size=n)
ayuda_financiera = np.random.choice([0, 1], size=n)

# Variable objetivo: Dropout
dropout = np.random.choice(['Sí', 'No'], size=n, p=[0.3, 0.7])  # 30% deserción

# Crear DataFrame
df = pd.DataFrame({
    'Edad': edad,
    'Genero': genero,
    'LugarOrigen': lugar_origen,
    'PromedioColegio': promedio_colegio,
    'AdmissionTest': admission_test,
    'PrimerSemestre': primer_semestre,
    'NivelSocioeconomico': nivel_socioeconomico,
    'Beca': beca,
    'Prestamo': prestamo,
    'AyudaFinanciera': ayuda_financiera,
    'Dropout': dropout
})

# Introducir valores nulos aleatoriamente (5% de los datos)
for col in df.columns[:-1]:  # no poner nulos en Dropout
    df.loc[df.sample(frac=0.05).index, col] = np.nan

# Introducir outliers en variables académicas
df.loc[df.sample(frac=0.02).index, 'PromedioColegio'] = 6.0  # fuera de rango
df.loc[df.sample(frac=0.02).index, 'PrimerSemestre'] = 0.0   # fuera de rango

# Guardar CSV
df.to_csv('dataset_sintetico_dropout.csv', index=False)
print("Dataset generado con éxito!")
