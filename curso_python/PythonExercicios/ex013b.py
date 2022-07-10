preco = float(input('Qual o preço do produto: R$'))
avista = preco - (preco * 10/100)
aprazo = preco + (preco * 8/100)
parcel = aprazo/5
print('Para pagamento à vista o preço tem 10% de desconto R${:.2f}'.format(avista))
print('Para pagamento à prazo o preço tem 8% de aumento R${:.2f}'
      '\ncom parcelamento em até 5x de R${:.2f}'.format(aprazo, parcel))
