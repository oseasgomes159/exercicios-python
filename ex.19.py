print('-=-'*20)
print('EMPRESTIMO CONSIGNADO FÁCIL')
print('-=-'*20)
emprestimo = float(input('Digite o valor do IMOVEL: '))
salario = float(input('Digite o valor do seu SALÁRIO: '))
parcela = int(input('Em quantos anos quer PARCELAR: '))
cal = emprestimo / (parcela * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$:{:.2f} em {} anos'.format(emprestimo, parcela),end='')
print(' A prestação será de {:.2f} '.format(cal))
if cal <= minimo:
    print('O emprestimo foi APROVADO')
else:
    print('O emprestimo foi NEGADO')
