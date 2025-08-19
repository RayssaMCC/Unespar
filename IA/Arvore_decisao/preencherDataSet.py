import pandas as pd
from datetime import datetime

# Lê a planilha Excel
df = pd.read_excel(r'') # Insira o caminho do arquivo aqui

mediana_Glucose = df['Glucose'].median()
mediana_BloodPressure = df['BloodPressure'].median()
mediana_SkinThickness = df['SkinThickness'].median()
mediana_Insulin = df['Insulin'].median()
mediana_BMI = df['BMI'].median()

df['Glucose'] = df['Glucose'].apply(lambda x: mediana_Glucose if x <= 0 else x)
df['BloodPressure'] = df['BloodPressure'].apply(lambda x: mediana_BloodPressure if x <= 0 else x)
df['SkinThickness'] = df['SkinThickness'].apply(lambda x: mediana_SkinThickness if x <= 0 else x)
df['Insulin'] = df['Insulin'].apply(lambda x: mediana_Insulin if x <= 0 else x)
df['BMI'] = df['BMI'].apply(lambda x: mediana_BMI if x <= 0 else x)

nome = f"dataset_alterado_mediana_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
df.to_excel(nome, index=False)

# Mostra as 5 primeiras linhas
print('Glucose: ')
print(mediana_Glucose)
print('SkinThickness: ')
print(mediana_SkinThickness)
print('Insulin: ')
print(mediana_Insulin)
print('BloodPressure: ')
print(mediana_BloodPressure)
print('BMI: ')
print(mediana_BMI)
print(df.head())
