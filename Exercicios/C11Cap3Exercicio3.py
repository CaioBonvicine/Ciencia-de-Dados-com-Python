nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))
if media >= 50:
    status = "AP"
else:
    status = "RP"

aluno = {"nome": nome, "media": media, "status": status}
print("\nDados do aluno:", aluno)