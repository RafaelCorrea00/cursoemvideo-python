from ex108 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade do {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 5%, temos {moeda.moeda(moeda.diminuir(p, 5))}')
