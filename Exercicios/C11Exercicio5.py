numero = int(input("Digite um número entre 1000 e 9999: "))

if 1000 <= numero <= 9999:
    print(f"Unidade: {numero // 1000}")
    print(f"Dezena: {(numero % 1000) // 100}")
    print(f"Centena: {(numero % 100) // 10}")
    print(f"Milhar: {numero % 10}")
else:
    print("Número inválido. Deve estar entre 1000 e 9999.")