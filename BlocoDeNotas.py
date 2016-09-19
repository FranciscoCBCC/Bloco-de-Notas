print("Classe BlocoDeNotas")

from Notas import Notas
import random

class BlocoDeNotas:
    notas = []
    #indice = 0
    def __init__(self):
        self.notasObj = Notas()
                
    def buscar(self):
        pass
        
    def adicionar_notas(self):
        #self.__class__.indice += 1
        texto = input("Digite o texto da nota: ")
        self.notasObj.setTexto(texto)
        titulo = input("Digite o titulo da nota: ")
        self.notasObj.setTitulo(titulo)
        
        #for i in range(10):
        #    id= random.random()
            
            
        def gera_random():
            return random.randrange(10)            
            
        id = gera_random()    
            
                   
        self.notasObj.setId(id)
        
        self.__class__.notas.append(self)
        
    def imprimir_notas(self, nota=None):
        if not nota:
            nota = self.notas #Deve ter uma lista para as notas
        for n in nota:
            print(n)
            
    
    def alterar_texto(self):
        pass
        
    def alterar_titulo(self):
        pass
        