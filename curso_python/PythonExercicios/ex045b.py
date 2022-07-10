from random import choice
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(jokenpo)
jogador = str(input('Qual é sua jogada? ')).upper().strip()
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
if jogador == computador:
    print('EMPATE')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print('PERDEU')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print('PERDEU')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print('PERDEU')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('VENCEU')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('VENCEU')
elif jogador == 'PEDRA' and computador == 'TESOURA':
    print('VENCEU')
else:
    print('JOGADA INVÁLIDA')
