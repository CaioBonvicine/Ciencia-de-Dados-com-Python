numero = int(input("Digite o número para ver sua tabuada: "))
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")