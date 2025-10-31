""" Detalhando strings e usando formato """

nomeCompleto = "Caio Comitre Rossi"
inicio = 5
fim = inicio + 6
print(nomeCompleto[inicio:fim])

# Entendendo o campo Input

nome = input("Qual o seu nome?: ")
sobrenome = input("Informe seu sobrenome: ")
print("Seu nome completo é: " + nome + " " + sobrenome)

# Calculadora primitiva =)

valor01 = int(input("Insira seu primeiro valor: "))
valor02 = input("Insira seu segundo valor: ")
# ou assim: valor = int(valor)

print(valor01 + int(valor02))