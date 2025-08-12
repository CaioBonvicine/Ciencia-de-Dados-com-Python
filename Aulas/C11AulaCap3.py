DBnames = ('Goku', 'Vegeta', 'Piccolo', 'Gohan', 'Trunks')
print('DBnames:', DBnames)
# O codigo acima é um exemplo de tupla, que é uma coleção ordenada e imutável de elementos.

print (DBnames[0 : 3]) # Acessando os três primeiros elementos da tupla
print (DBnames[2 : 5]) # Acessando os três últimos elementos da tupla
print (DBnames[-1])    # Acessando o último elemento da tupla

print(len(DBnames))  # Imprimindo o tamanho da tupla
print(max(DBnames))  # Imprimindo o maior elemento da tupla
print(min(DBnames))  # Imprimindo o menor elemento da tupla


print()

# Agora para listas!
DBnames_list = ['Goku', 'Vegeta', 'Piccolo', 'Gohan', 'Trunks']
print('DBnames:', DBnames_list)

DBnames_list.append('Bulma')  # Adicionando um novo elemento à lista
print('Updated DBnames:', DBnames_list)
DBnames_list[1] = 'Frieza'  # Alterando o segundo elemento da lista
print('Altered DBnames:', DBnames_list)
del DBnames_list[3]  # Removendo o quarto elemento da lista
print('After deletion:', DBnames_list)
DBnames_list.remove('Trunks')  # Removendo 'Trunks' da lista
print('After removing Trunks:', DBnames_list)

print()

#Agora para conjuntos!
DBnames_set = {'Goku', 'Vegeta', 'Piccolo', 'Gohan', 'Trunks'}
print('DBnames:', DBnames_set)

DBnames_set.add('Bulma')  # Adicionando um novo elemento ao conjunto
print('Updated DBnames:', DBnames_set)
#Conjuntos não permitem duplicatas, então se você tentar adicionar um elemento já existente, nada acontecerá.
#Conjuntos também não mantêm a ordem dos elementos.
DBnames_set.remove('Trunks')  # Removendo 'Trunks' do conjunto
print('After removing Trunks:', DBnames_set)



