salario = float(input('Digite o seu salário R$: '))
if salario >= 1250:
    aumento = salario * 10 / 100
    sal = aumento + salario
else:
    aumento = salario * 15 / 100
    sal = aumento + salario

print('Seu salário é R$: {:.2f}, e o aumento foi de R$: {:.2f}'.format(salario, aumento))
print('Portanto o valor total ficará R$: {}'.format(sal))