print("Classe BlocoDeNotas")

from Notas import Notas

class BlocoDeNotas:
    notas = []
    def __init__(self):
        self.notasObj = Notas()
                
    def buscar(self):
        pass
        
    def adicionar_notas(self):
        texto = input("Digite o texto da nota: ")
        self.notasObj.setTexto(texto)
    
    def alterar_texto(self):
        pass
        
    def alterar_titulo(self):
        pass
        