# 📊 Previsão de Vendas com Regressão Linear

## 📌 Descrição do Projeto

Este projeto tem como objetivo prever as vendas futuras de produtos de uma rede de lojas de tintas utilizando **regressão linear simples**.

Foram analisados dados de vendas do ano de 2023 para diferentes produtos, com o intuito de prever os meses futuros (13, 14 e 15).

---

## 🤖 Tipo de Análise de Machine Learning

Este projeto utiliza **Aprendizado Supervisionado**.

✔️ Justificativa:
Os dados possuem uma variável de entrada (mês) e uma variável alvo (vendas), permitindo treinar um modelo que aprende a relação entre elas.

---

## 📊 Metodologia

A regressão linear simples segue a equação:

[
y = ax + b
]

Onde:

* **y** = vendas previstas
* **x** = mês
* **a** = inclinação (taxa de crescimento)
* **b** = intercepto

---

## 📈 Resultados por Produto

### 🟦 Tinta Acrílica

* Tendência: Crescimento forte
* R² ≈ 0.91 (alta confiabilidade)

Previsões:

* Mês 13 → ~420
* Mês 14 → ~440
* Mês 15 → ~460

---

### 🟩 Tinta Esmalte

* Tendência: Crescimento linear
* R² ≈ 0.98 (muito confiável)

Previsões:

* Mês 13 → ~210
* Mês 14 → ~220
* Mês 15 → ~230

---

### 🟨 Tinta Látex

* Tendência: Crescimento constante
* R² ≈ 0.99 (excelente)

Previsões:

* Mês 13 → ~320
* Mês 14 → ~330
* Mês 15 → ~340

---

### 🟥 Tinta Spray

* Tendência: Crescimento moderado
* R² ≈ 0.97

Previsões:

* Mês 13 → ~135
* Mês 14 → ~140
* Mês 15 → ~145

---

### 🟪 Tinta PVA

* Dados limitados (apenas 2 meses)
* R² não confiável

Previsões:

* Crescimento estimado simples

---

## 📊 Previsão por Trimestre

| Produto        | Próximo Trimestre (13-15) | Tendência    |
| -------------- | ------------------------- | ------------ |
| Tinta Acrílica | ~1320                     | Forte alta   |
| Tinta Esmalte  | ~660                      | Crescimento  |
| Tinta Látex    | ~990                      | Estável alta |
| Tinta Spray    | ~420                      | Crescimento  |

---

## 📉 Conclusões

* Todos os produtos apresentam tendência de crescimento.
* Tinta Látex possui o comportamento mais estável.
* Tinta Acrílica apresenta maior aceleração de vendas.
* Modelos com mais dados possuem maior confiabilidade (R² alto).

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib / Seaborn
* Scikit-learn

---

## 📎 Como Executar

```bash
pip install pandas numpy matplotlib scikit-learn
python analise.py
```

---

## 📌 Resultado Final

O modelo conseguiu prever as vendas futuras com boa precisão para a maioria dos produtos, validado pelo coeficiente R².

---

## 👨‍🏫 Autor

Projeto desenvolvido para avaliação de Machine Learning.
