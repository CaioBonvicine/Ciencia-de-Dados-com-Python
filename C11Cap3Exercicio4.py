pessoas = []
for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    peso = float(input(f"Digite o peso de {i+1}ª pessoa em kg: "))
    pessoas.append((peso, nome))

print("\nPessoa mais pesada:", max(pessoas))
print("Pessoa mais leve:", min(pessoas))
    
    



