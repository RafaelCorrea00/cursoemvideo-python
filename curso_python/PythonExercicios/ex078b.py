# Minha solução sem ver a resolução do professor
valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')
for c1, v1 in enumerate(valores):
    if v1 == max(valores):
        print(f'{c1}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for c2, v2 in enumerate(valores):
    if v2 == min(valores):
        print(f'{c2}...', end=' ')
