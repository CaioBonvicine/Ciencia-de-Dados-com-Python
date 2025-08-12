while True:
    sexo = input("Digite o seu sexo (M para masculino ou F para feminino): ").upper()
    
    if sexo == 'M':
        print("Sexo: Masculino")
        break
    elif sexo == 'F':
        print("Sexo: Feminino")
        break
    else:
        print("Opção inválida")