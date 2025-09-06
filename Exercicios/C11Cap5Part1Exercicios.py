import pandas as pd

dic1 = {'Java': 16.25, 'C': 16.04, 'Python': 9.85}
dic2 = {'C': 16.21, 'Python': 12.12, 'Java': 11.68}
seriesAno1 = pd.Series(dic1)
seriesAno2 = pd.Series(dic2)

Ano1Total = seriesAno1.sum()
Ano2Total = seriesAno2.sum()

print("Porcentagem Ano1: ", Ano1Total)
print("Porcentagem Ano2: ", Ano2Total)

print()

diferenca = seriesAno2 - seriesAno1
print(diferenca)

print()

positivo = diferenca[diferenca > 0]
print(positivo)

print()

primeira_previsao = seriesAno1 + diferenca
segunda_previsao = primeira_previsao + diferenca

print(segunda_previsao.nlargest(1))
