import numpy as np
import random

campo = np.zeros((2, 2), dtype=int)
linha = random.randint(0, 1)
coluna = random.randint(0, 1)
campo[linha, coluna] = 1

i = 0


#iniciando jogo!

while True:
    i += 1
    linha_jogada = int(input("Digite a linha (0 ou 1): "))
    coluna_jogada = int(input("Digite a coluna (0 ou 1): "))

    if i == 3:
        print("Você Venceu!")
        break

    if campo[linha_jogada, coluna_jogada] == 1:
        print("BOOM!!! Você perdeu!")
        break
    else:
        print("Essa você escapou! Continue jogando.")
