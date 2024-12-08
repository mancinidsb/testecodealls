class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.imc=None
    
    def calcula_imc(self):
        imc = self.peso/(self.altura*self.altura)
        self.imc = round(imc, 2)
        return self.imc 
    
    def __str__(self):
        return f"nome: {self.nome} | idade: {self.idade} | peso: {self.peso} | altura: {self.altura} -> IMC: {self.calcula_imc()}"