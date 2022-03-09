vel = float(input('Digite a Velocidade em KM/h: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você atingiu o limite da velocidade permitida')
    print('Sua multa é no valor de R$: {:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança!')