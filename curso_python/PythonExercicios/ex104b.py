def leiaInt(num):
    while True:
        n = input(num)
        if n.isnumeric():
            num = int(n)
            return num
        else:
            print('\033[31mERRO! Número inválido. Tente novamente.\033[m')


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
