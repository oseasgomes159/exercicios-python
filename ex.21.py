num1 = int(input('Digite o Primeiro número: '))
num2 = int(input('Digite o Segundo número: '))
if num1 > num2:
    print('O número {} é o Maior!'.format(num1))
elif num2 > num1:
    print('O número {} é o Maior'.format(num2))
else:
    print('Os números são iguais.')
