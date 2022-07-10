from ex107 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade do R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentado 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Reduzindo 5%, temos R${moeda.diminuir(p, 5)}')
