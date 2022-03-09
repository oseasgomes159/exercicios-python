print('=-='*10)
print('ESCOLA OSEIAS GOMES')
print('=-='*10)
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando as notas {:.1f} e {:.1f} sua média será: {:.1f}'.format(nota1, nota2, media))
if media >= 7:
    print('PARABÉNS VOCÊ ESTÁ APROVADO!')
elif media > 5 and media < 7:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO, ESTUDE MAIS!')
else:
    print('VOCÊ FOI REPROVADO!')
