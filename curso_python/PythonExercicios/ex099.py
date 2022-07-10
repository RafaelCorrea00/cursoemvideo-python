def maior(* num):
    cont = mai = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
