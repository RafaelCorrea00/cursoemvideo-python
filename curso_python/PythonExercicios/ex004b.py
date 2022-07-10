a = input('Digite algo:')
print('Qual é o tipo primitivo?', type(a))
print('Só tem espaços? {}. É um número? {}. É alfabético? {}. É alfanumérico? {}. Está em maiúsculas? {}. Está em '
      'minúsculas? {}. Está capitalizada? {}.'.format(a.isspace(), a.isnumeric(), a.isalpha(), a.isalnum(), a.isupper(), a.islower(), a.istitle()))
