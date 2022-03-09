from datetime import date
atual = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = atual - ano
print('O atleta tem {} Ano(s).'.format(idade))
if idade <= 9:
    print('Você é um nadador MIRIM!')
elif idade <= 14:
    print('Você é um nadador INFANTIL!')
elif idade <= 19:
    print('Você é um nadador JUNIORS!')
elif idade <= 25:
    print('Você é um nadador SÊNIOR!')
else:
    print('Você é um nadador MASTER!')
