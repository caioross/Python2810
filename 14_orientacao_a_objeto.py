class Carro :
    def __init__ (self, modelo, cor) :
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0 # carro começa parado

    def acelerar(self, incremento) :
        """ Acelera o carro, aumentando a velocidade."""
        self.velocidade += incremento 
        # old version: self.velocidade = self.velocidade + incremento
        print(f"O carro {self.modelo} acelerou para {self.velocidade} Km/h.")    
    
    def parar(self) :
        self.velocidade = 0
        print(f"O carro {self.modelo} parou.")
        
    def desacelerar(self, decremento) :
        """Desacelerar o carro de passo em passo """
        while self.velocidade > 0 :
            passo = min(10, self.velocidade) # reduz 10 ou o que faltar
            self.velocidade -= passo
            print(f"O carro {self.modelo} desacelerou para {self.velocidade} Km/h. ")
        if self.velocidade == 0 :
            print(f"O carro {self.modelo} parou.")
        
        
carro_instrutor = Carro("Suzuki Jimny", "Amarelo")
carro_instrutor.acelerar(20)
carro_instrutor.acelerar(100)
carro_vicente = Carro("BYD", "Cinza")
carro_vicente.acelerar(90)
carro_instrutor.desacelerar(20)