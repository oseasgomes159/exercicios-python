num = int(input('Digite um número INTEIRO: '))
print('''Escolha uma das bases para a Conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
posi = int(input('Sua opção: '))
if posi == 1:
    print('{} Convertido para BINÁRIO é igual à: {}'.format(num, bin(num)))
elif posi == 2:
    print('{} Convertido para OCTAL é igual à: {}'.format(num, oct(num)))
elif posi == 3:
    print('{} Convertido para HEXADECIMAL é igual à: {}'.format(num, hex(num)))
else:
    print('Opção invalida. Tente novamente!')