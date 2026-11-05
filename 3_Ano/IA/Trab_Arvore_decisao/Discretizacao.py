import pandas as pd
from datetime import datetime

df = pd.read_excel(r'')  # Insira o caminho do arquivo aqui

def Pregnancies(x):
    if x == 0:
        return 'Nuligesta'
    elif x == 1:
        return 'Primigesta'
    elif x == 2:
        return 'Segundigesta'
    elif x > 2 and x < 5:
        return 'Multigesta'
    else:
        return "Grande Multigesta"
    
def Glucose(x):
    if x <= 70:
        return 'Baixa'
    elif x > 70 and x <= 140:
        return 'Normal'
    elif x > 140 and x <= 199:
        return 'Pré-diabetes'
    else:
        return 'Diabetes'


def BloodPressure(x):
    if x <= 60:
        return 'Baixa'
    elif x > 60 and x <= 80:
        return 'Normal'
    elif x > 80 and x <= 89:
        return 'Hipertensão 1'
    else:
        return 'Hipertensão 2'
    
def SkinThickness(x):
    if x < 10:
        return 'Baixa'
    elif x >= 10 and x <= 28:
        return 'Normal'
    else:
        return 'Obesidade'

def BMI(x):
    if x < 18.5:
        return 'Baixo'
    elif x >= 18.5 and x < 25:
        return 'Normal'
    elif x >= 25 and x < 30:
        return 'Sobrepeso'
    elif x >= 30 and x < 35:
        return 'Obesidade'
    elif x >= 35 and x < 40:
        return 'Obesidade Severa'
    else:
        return 'Obesidade Mórbida'

def Insulin(x):
    if x <= 15:
        return 'Baixo'
    elif x > 15 and x <= 60:
        return 'Normal'
    elif x > 60 and x <= 100:
        return 'Alta'
    else:
        return 'Muito Alta'
    
def DiabetesPedigreeFunction(x):
    if x <= 0.25:
        return 'Baixo'
    elif x > 0.25 and x <= 0.5:
        return 'Moderado'
    else:
        return 'Alto'
    
def Age(x):
    if x <= 9:
        return 'Infância'
    elif x > 9 and x <= 19:
        return 'Adolescência'
    elif x >= 20 and x < 35:
        return 'Jovem'
    elif x >= 35 and x < 45:
        return 'Adulta'
    elif x >= 45 and x <= 51:
        return 'Climatério'
    else:
        return 'Pós-menopausa'

df['Pregnancies'] = df['Pregnancies'].apply(Pregnancies)
df['Glucose'] = df['Glucose'].apply(Glucose)
df['BloodPressure'] = df['BloodPressure'].apply(BloodPressure)
df['BMI'] = df['BMI'].apply(BMI)
df['Insulin'] = df['Insulin'].apply(Insulin)
df['SkinThickness'] = df['SkinThickness'].apply(SkinThickness)
df['DiabetesPedigreeFunction'] = df['DiabetesPedigreeFunction'].apply(DiabetesPedigreeFunction)
df['Age'] = df['Age'].apply(Age)

nome = f"dataset_alterado_categorizado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
df.to_excel(nome, index=False)

print(df.head())
