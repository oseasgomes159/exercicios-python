from random import randint
from time import sleep
print('=-='*20)
print('ESTOU PENSANDO EM UM NÚMERO TENTE ADIVINHAR QUAL É...')
print('=-='*20)
num = int(input('Digite um número para jogar: ')) # JOGADOR DIGITA O NUMERO
sorteio = randint(0,10) # COMPUTADOR SORTEIA
print('PROCESSANDO...')
sleep(2)
print('O número sorteado foi {} e oque você digitou foi {}'.format(sorteio, num)) #APARECE A RESPOSTA
if num == sorteio:
    print('Você acertou o número sorteado Parabéns!')
else:
    print('Você errou tente novamente...')
print('=-='*20)