print('='*15,'LOJAS OSEIAS','='*15)
preço = float(input('Preço das Compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à Vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
desc = int(input('Qual é sua opção? '))
if desc == 1:
    vista = preço * 10 / 100
    final = preço - vista
    print('O valor do desconto é R${:.1f} e o valor total que irá pagar é R${:.1f}'.format(vista,final))
elif desc == 2:
    vista = preço * 5 / 100
    final = preço - vista
    print('O valor do desconto é R${:.1f} e o valor total que irá pagar é R${:.1f}'.format(vista,final))
elif desc == 3:
    print('O valor não irá alterar você ira pagar R${}'.format(preço))
elif desc == 4:
    parc = int(input('Em quantas vezes quer parcelar? '))
    vista = preço * 20 / 100
    final = (preço + vista) / parc
    inicial = preço + vista
    print('Sua compra será parcelada em {}x de R${} com JUROS\n'
          'O preço inicial era R${} e passou para R${}'.format(parc,final, preço, inicial))


#pode fazer com vista = preço - (preço * total 10 / 100) se nao quiser as informações adicionais e simplificar o codigo
