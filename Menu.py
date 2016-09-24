import sys
from BlocoDeNotas import BlocoDeNotas

class Menu:
    def __init__(self):
        self.blocodenotas = BlocoDeNotas()
        self.escolhas = {
        "1": self.blocodenotas.imprimir_notas,
        "2": self.blocodenotas.buscar_notas,
        "3": self.blocodenotas.adicionar_notas,
        "4": self.blocodenotas.remover_notas,
        "5": self.blocodenotas.modificar_notas,
        "6": self.sair
        }
        
    def apresentar_menu(self):
        print("""
        Menu
        1. Imprimir Notas
        2. Buscar Notas
        3. Adicionar Notas
        4. Remover Notas
        5. Modificar Notas
        6. Sair        
        """)

    def executar(self): #É executado eternamente apresentado o menu com as escolhas para selecionar uma opção
        while True: #Verdadeiro pra sempre
            self.apresentar_menu() #mostra o metodo apresentar menu
            escolha = input("escolha uma opcao: ") #Tipo um scanf no C; Antigo raw_input
            acao = self.escolhas.get(str(escolha)) #Get=Busca no dicionario, é um metodo do python
            if acao:
                acao()
            else:
                print ("{0} nao foi uma escolha valida.".format(escolha))
         
    def sair(self):
        print ("Saindo ...")
        sys.exit(0)
    
if __name__ == "__main__": #Como se fosse um main
    m = Menu()
    m.executar()