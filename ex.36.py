from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for letra in range(1,7+1):
    ano = int(input('Em que ano a {}º pessoa nasceu: '.format(letra)))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas Maiores de Idade'.format(totmaior))
print('E também tivemos {} pessoas Menores de Idade'.format(totmenor))
