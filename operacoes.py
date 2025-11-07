# Função para somar
def somar(a, b):
    return a + b

# Função para Subtrair
def subtrair(a, b):
    return a - b

# Função para dividir
def dividir(a, b):
    if b == 0 : # verifica se o divisor for zero
        raise ValueError("Não é possivel dividir por zero!") # Levanta um erro se b for 0
    return a / b

# Função para multiplicar
def multiplicar(a, b):
    return a * b





