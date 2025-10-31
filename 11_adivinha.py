from random import randint

print("### Iniciando o Jogo ###")
dificuldade ='''
[1] Facil (10 Chances)
[2] Médio (5 Chances)
[3] Dificil (3 Chances) 
'''
print(dificuldade)
escolhadificuldade = input('Escolha a dificuldade: ')

if escolhadificuldade == '1' :
    chances = 10
if escolhadificuldade == '2' :
    chances = 5
if escolhadificuldade == '3' :
    chances = 3

random = randint(0,100)
chute = 0
#chances = 10 

while chute != random :
    chute = input('Chute um numero entre 0 e 100:')
    if chute.isnumeric() :
        chute = int(chute)
        chances = chances - 1
        if chute == random :
            print('-------')
            print('Parabéns, você venceu! O numero era {} e você ainda tinha {} chances'.format(random,chances))
            print('-------')
            break
        else:
            print('')
            if chute > random :
                print('Você errou! Dica: É um numero menor')
            else :
                print('Você errou! Dica: É um numero maior')
            print('Você ainda possui {} chances'.format(chances))
            print('')
        if chances == 0 :
            print('')
            print('Suas chances acabaram, e você perdeu')
            print('O valor era: {}'.format(random))
            print('')
            break
print("### Fim do Jogo ###")
            
            