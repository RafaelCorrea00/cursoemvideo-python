galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO!Responda apenas S ou N.')
    if resp == 'N':
        break
    print('-' * 30)
# Até a linha 24 é a leitura dos dados
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f}')
print('C) As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
# Da linha 26 até a 42 são os resultados
