palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras: # analisa cada elemento da tupla
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p: # analisa cada letra de p
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
