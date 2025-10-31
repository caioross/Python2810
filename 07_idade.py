""" Hora do Exercicio """
# perguntar o ano em que o usuario nasceu
# perguntar o ano em que estamos
# informar a idade

''' Bonus Lógico '''
# Perguntar para o usuario se ele deseja testar novamente
# caso sim refazer o teste
# caso não fim do programa

executar = True
while executar:
    anoNasc = input("Em que ano você nasceu: ")
    anoAtual = input("Em que ano estamos: ")
    idade = int(anoAtual) - int(anoNasc)
    print('Você tem ' + str(idade) + ' anos.')
    opcao = input("\nDeseja testar novamente? \nSim ou Não?")
    if opcao == "Não" :
        executar = False
