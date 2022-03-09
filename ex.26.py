peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em METROS: '))
imc = peso / (altura **2)
print('Seu IMC é: {:.1f}'.format(imc))
if imc <= 18.5:
    print('Sua Classificação (MAGREZA)')
elif imc > 18.5 and imc < 24.9:
    print('Sua Classificação (NORMAL)')
elif imc > 25.0 and imc < 29.9:
    print('Sua Classificação (SOBREPESO)')
elif imc > 30 and imc < 39.9:
    print('Sua Classificação (OBESIDADE)')
else:
    print('Sua Classificação (OBESIDADE GRAVE)')
