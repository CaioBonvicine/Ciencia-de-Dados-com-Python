grupo = []

n = int(input("Digite a quantidade de pessoas: "))

for i in range(n):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    sexo = input(f"Digite o sexo da {i+1}ª pessoa (M/F): ").strip().upper()
    grupo.append({"nome": nome, "idade": idade, "sexo": sexo})


mediaIdade = sum(p["idade"] for p in grupo) / n
print(f"\nMédia de idade: {mediaIdade} anos")

mulheres20 = sum(1 for p in grupo if p["sexo"] == "F" and p["idade"] < 20)
print(f"Número de mulheres com menos de 20 anos: {mulheres20}")
