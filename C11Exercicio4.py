Km = float(input("Digite a distância da viagem em Km: "))

if Km <= 200:
    preco = Km * 0.50
else:
    preco = Km * 0.45

print(f"Preço = R${preco:.2f}")