#Nome: Kaue Henrique dos Santos Data: 04/04/2024
# 
# 
# 
# 
# ##########################################################################
import copy

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'
    
    def clone(self):
        return copy.copy(self)
    
class PessoaManager:
    def __init__(self):self.pessoa = {}
    
    def add_pessoa(self, nome, idade, id):
        pessoa = Pessoa(nome, idade)
        self.pessoa[id] = pessoa
        
    def get_pessoa(self, id):
        return self.pessoa[id].clone()
    
#####################################################################
manager = PessoaManager()

#Adiconar pessoas
manager.add_pessoa("Kaue", 19, 1)
manager.add_pessoa("Kawan", 20, 2)


#Clonar Pessoas
pessoa1 = manager.get_pessoa(1)
pessoa2 = manager.get_pessoa(2)

#Modificando informações
pessoa1.idade = 18
pessoa2.nome = "guilherme"
pessoa2.idade = 55

#Imprimir resultados
print(manager.get_pessoa(1))
print(manager.get_pessoa(2))
print(pessoa1)
print(pessoa2)
