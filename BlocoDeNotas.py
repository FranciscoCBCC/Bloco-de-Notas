print("Classe BlocoDeNotas")

from Notas import Notas
import random

class BlocoDeNotas:

    def __init__(self):
        self.notas = []
        self.indice = 0
                
    def buscar(self):
        pass
        
    def adicionar_notas(self):
        texto = input("Digite o texto da nota: ")
        titulo = input("Digite o titulo da nota: ")
        id = random.randrange(0, 100);    
        data = input("Digite a data da nota: ")
        self.indice += 1
        self.notas.append(Notas(id, texto, titulo, data, self.indice))
            
    def imprimir_notas(self, nota=None):
        if not nota:
            nota = self.notas #Deve ter uma lista para as notas
        for n in nota:
            print(n)
            
    
    def alterar_texto(self):
        pass
        
    def alterar_titulo(self):
        pass
        