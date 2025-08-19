import pandas as pd

# Caminho do seu arquivo CSV
caminho_csv = "diabetes.csv"

# Lê o arquivo CSV
df = pd.read_csv(caminho_csv)

# Salva como Excel
df.to_excel("dataSet.xlsx", index=False)

print("Arquivo Excel 'dataSet.xlsx' criado com sucesso!")
