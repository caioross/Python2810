def divisao(a, b):
    try:
        # Tentando dividir os dois numeros
        resultado = a / b
        print(f"O Resultado de {a} por {b} é: {resultado}")
    except ZeroDivisionError :
        # Se houver um erro de divisão por zero o codigo dentro do except é executado
        print("Erro: Não é possivel dividir por zero")
    except TypeError :
        # Caso os parametros fornecidos não sejam numeros
        print("Erro: Ambos os valores devem ser numeros.")
    except Exception as erro:
        # Captura qualquer outro tipo de exceção que nao tenha sido tratada nos anteriores
        print(f"Erro inesperado: {erro}")
    else:
        # É executado se o codigo dentro do try for bem-sucedido(sem erros)
        print("Divisão foi realizada com sucesso!")
    finally:
        # Sempre é executado, idependente de erro ou sucesso
        print("O processo de divisão foi concluido.")
        
# Teste 01: Divisão Normal
divisao(10,2)

# Teste 02: Divisão por zero
divisao(10,0) 

# Teste 03: Divisão com tipos invalidos
divisao(10, "dois")

# Teste 04: Divisão com erro inesperado
divisao("dez", 2)
