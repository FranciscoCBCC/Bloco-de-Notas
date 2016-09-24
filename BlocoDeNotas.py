print("Classe BlocoDeNotas")

from Notas import Notas
import random
import datetime

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
        self.indice += 1
        self.data = str(datetime.datetime.now())[:19]
        self.notas.append(Notas(id, texto, titulo, self.data, self.indice))
            
    def imprimir_notas(self, nota=None):
        #if not nota:
        if (self.indice != 0):
            nota = self.notas #Deve ter uma lista para as notas
            for n in nota:
                print(n)
        else:
            print("Não há notas")
     
    def buscar_notas(self):
        if (self.indice != 0):
            id = int(input("Digite o ID da nota: "))
            #nota = self.blocodenotas.buscar(filtro)
            #self.imprimir_notas(nota)     
            for i in self.notas:
                if id == i.getId():
                    print(i)
                    break
                else:
                    print("ID nao encontrado")
        else:
            print("Não há notas")
    
    def remover_notas(self):
        if (self.indice != 0):
            self.indice -= 1
            id = int(input("Digite o ID da nota: "))
            for i in self.notas:
                if id == i.getId():
                    print("A nota foi removida:")
                    self.notas.remove(i)
        else:
            print("Não há notas")

    
    def alterar_texto(self):
        pass
        
    def alterar_titulo(self):
        pass
        