""" Funções no Python """
def minhaFuncao() :
    print("Hello World!")
    
minhaFuncao()
minhaFuncao()

cidades = ['São Paulo','Recife','Dubai','Poá','Vitória de Santo','Goiania']
contador = 0

def minhaFuncaoMelhorada(citi, calcule) :
    print(str(calcule) + ' - ' + citi)

for cidade in cidades :
    contador = contador + 1
    minhaFuncaoMelhorada(cidade, contador)
    
minhaFuncaoMelhorada('Mogi das Cruzes', 3)