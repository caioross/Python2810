""" Trabalhando com Loopings """

cidades = ['São Paulo','Recife','Dubai','Poá','Vitória de Santo','Goiania']

# Looping : FOR

for cidade in cidades :
    print(cidade)
    
palavra = "Caio"
contador = 0

for letra in palavra :
    print(str(contador) + ' - ' + letra)
    contador = contador + 1
    
print(cidades[2])

# Looping: WHILE

botaoExecutar = True
contador = 0

while botaoExecutar :
    print(contador)
    contador = contador + 1
    if contador >= 10 :
        botaoExecutar = False

