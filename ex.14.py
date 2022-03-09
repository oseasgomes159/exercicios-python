from time import sleep
valor = float(input('Digite quantos KM será a viagem: '))
print('Estamos calculando o custo da viagem...')
sleep(2)
if valor <= 200:
    total = valor * 0.50
else:
    total = valor * 0.45
print('O valor da Passagem será de R$: {:.2f}\nTenha uma boa viagem'.format(total))
