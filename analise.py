import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Carregar dados
df = pd.read_csv("dados.csv")

resultados = []

for produto in df["Produto"].unique():
    dados = df[df["Produto"] == produto]

    X = dados["Mês"].values.reshape(-1,1)
    y = dados["Vendas (unidades)"].values

    if len(X) < 3:
        continue

    modelo = LinearRegression()
    modelo.fit(X, y)

    y_pred = modelo.predict(X)
    r2 = r2_score(y, y_pred)

    # previsão meses futuros
    futuros = np.array([13,14,15]).reshape(-1,1)
    previsoes = modelo.predict(futuros)

    for i, mes in enumerate([13,14,15]):
        resultados.append([produto, mes, None, previsoes[i], r2])

# salvar resultados
df_result = pd.DataFrame(resultados, columns=["Produto","Mês","Vendas reais","Vendas previstas","R²"])
df_result.to_csv("resultados.csv", index=False)

print(df_result)
