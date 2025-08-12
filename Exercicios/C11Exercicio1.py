name = input("Escreva seu nome completo: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

only_name = name.replace(" ", "")

print("Numero de caracteres:", len(only_name))

name_parts = name.split()

changed_name = ' '.join(name_parts[:-1]) + " do Inatel"

print("Nome modificado:", changed_name)