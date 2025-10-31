executar = True

while executar :
    escolhas = '''
    [1] ou [+] para Somar
    [2] ou [-] para Subtrair
    [3] ou [*] para Multiplicar
    [4] ou [/] para Dividir
    [5] para Sair
    (ou digite sua opção: Somar / Subtrair / Multiplicar / Dividir / Sair)
    '''
    print(escolhas)
    operador = input("Qual sua opção?: ") 
    valor01 = int(input("Escolha o primeiro numero: "))
    valor02 = int(input("Escolha o segundo numero: "))
    textofinal = '''
    Deseja realizar outro calculo?:
    [1] Não, desejo sair!
    [2] Sim, desejo realizar outro calculo.
    '''
    
    # Soma
    if operador == "1" or operador == "+" or operador == "Somar" :
        resultado = valor01 + valor02
        print("O resultado é: " + str(resultado))
        print(textofinal)
        escolhafinal = input("Qual sua escolha: ")
        if escolhafinal == "1" :
            executar = False
            
    # Subtração     
    if operador == "2" or operador == "-" or operador == "Subtrair" :
        resultado = valor01 - valor02
        print("O resultado é: " + str(resultado))
        print(textofinal)
        escolhafinal = input("Qual sua escolha: ")
        if escolhafinal == "1" :
            executar = False
            
    # Multiplicação
    if operador == "3" or operador == "*" or operador == "Multiplicar" :
        resultado = valor01 * valor02
        print("O resultado é: " + str(resultado))
        print(textofinal)
        escolhafinal = input("Qual sua escolha: ")
        if escolhafinal == "1" :
            executar = False

    # Divisão
    if operador == "4" or operador == "/" or operador == "Dividir" :
        resultado = valor01 / valor02
        print("O resultado é: " + str(resultado))
        print(textofinal)
        escolhafinal = input("Qual sua escolha: ")
        if escolhafinal == "1" :
            executar = False

    # Sair     
    if operador == "5" or operador == "Sair" :
        print("Obrigado por usar minha calculadora!")
        executar = False


        
        