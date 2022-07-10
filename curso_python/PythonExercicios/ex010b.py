real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/5.40
euro = real/6.11
libra = real/7.36
franco = real/5.89
iene = real/0.047
bitcoin = real/232974.16
print('Com R${:.2f} você pode comprar\n'
      'US${:.2f}\nEU${:.2f}\n£${:.2f}\nFR${:.2f}\nYE${:.2f}\nBC${:.6f}'
      .format(real, dolar, euro, libra, franco, iene, bitcoin))
