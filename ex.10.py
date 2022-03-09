frase = str(input('Digite uma Frase: ')).upper().strip()
print('A frase {} Contem\n {} Letras (A)'.format(frase, frase.count('A')))
print('A primeira letra (A) apareceu na {} posição'.format(frase.find('A')+1))
print('A última letra (A) apareceu na {} posição'.format(frase.rfind('A')+1))