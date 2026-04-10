import pandas as pd
from mlxtend.frequent_patterns import apriori

# Abre o arquivo .csv
df = pd.read_csv("Aula 26/pedidos_e_produtos.csv")

# Transforma em um mapa de bits
mapa_bits = pd.get_dummies(df.set_index('order_id')['product_name']).groupby(level=0).max()

# Calcula os itens frequentes usando o algoritmo apriori com suporte mínimo 5%
itens_frequentes = apriori(mapa_bits, min_support=0.01, use_colnames=True)

# Mostra os resultados
print(itens_frequentes)
