n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1  #O fator nulo de soma e subtração é 0 e o de multiplicação é 1
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c                          #ou f = f * c
    c -= 1                          #menos 1 do c
print('{}'.format(f))
