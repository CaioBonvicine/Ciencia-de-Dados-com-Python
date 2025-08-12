teams_list = ['Real Madrid', 'Liverpool', 'Bayern Munich', 'Barcelona', 'Juventus']

print("3 primeiros:", teams_list[:3])

print("Últimos 2:", teams_list[-2:])

ordem_alfabetica = sorted(teams_list)
print("Ordem alfabética:", ordem_alfabetica)

posicao_barcelona = teams_list.index('Barcelona') + 1
print("Barcelona está na posição:", posicao_barcelona)