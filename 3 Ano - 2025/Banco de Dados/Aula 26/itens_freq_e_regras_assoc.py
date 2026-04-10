import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Abre o arquivo .csv
df = pd.read_csv("Aula 26/pedidos_e_produtos.csv")

# Transforma em um mapa de bits
mapa_bits = pd.get_dummies(df.set_index('order_id')['product_name']).groupby(level=0).max()

# Calcula os itens frequentes usando o algoritmo apriori com suporte mínimo 1%
itens_frequentes = apriori(mapa_bits, min_support=0.01, use_colnames=True)

# Calcula regras de associação com confiança 10%
regras_assoc = association_rules(itens_frequentes, metric="confidence", min_threshold=0.1)

# Mostra os resultados
print(itens_frequentes)
print(regras_assoc)
