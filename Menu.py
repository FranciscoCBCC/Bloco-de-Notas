import sys
import datetime

class BlocoDeNotas:
    pass

class Menu:
    def __init__(self):
        self.blocodenotas = BlocoDeNotas()
        self.escolhas = {
        "1": self.imprimir_notas,
        "2": self.buscar_notas,
        "3": self.adicionar_notas,
        "4": self.modificar_notas,
        "5": self.sair
        }
        
    def apresentar_menu(self):
        print("""
        Menu
        1. Imprimir Notas
        2. Buscar Notas
        3. Adicionar Notas
        4. Modificar Notas
        5. Sair        
        """)

    def executar(self): #É executado eternamente apresentado o menu com as escolhas para selecionar uma opção
        while True: #Verdadeiro pra sempre
            self.apresentar_menu #mostra o metodo apresentar menu
            escolha = raw_input("escolha uma opcao: ") #Tipo um scanf no C
            acao = self.escolhas.get(str(escolha)) #Get=Busca no dicionario, é um metodo do python
            if acao:
                acao()
            else:
                print ("{0} nao foi uma escolha valida.".format(escolha))
                
    def imprimir_notas(self, nota=None):
        if not nota:
            nota = self.blocodenotas.notas #Deve ter uma lista para as notas
        for n in nota:
            print("{0}: {1}\n{2}".format(n.id,n.titulo, n.texto))
        
    def buscar_notas(self):
        filtro = raw_input("Digite o ID da nota: ")
        nota = self.blocodenotas.buscar(filtro)
        self.imprimir_notas(nota)
    
    def adicionar_notas(self):
        texto = raw_input("Digite o texto nota: ")
        self.blocodenotas.nova_nota(texto)

    def modificar_notas(self):
        id = int(raw_input("Digite o ID da nota: ")) #Faz um cast/conversao para inteiro int()
        texto = raw_input("Digite o novo texto: ")
        titulo = raw_input("Digite o novo titulo: ")
    
        if texto:
            self.blocodenotas.alterar_texto(id, texto)
        if titulo:
            self.blocodenotas.alterar_titulo(id, titulo)
        
    def sair(self):
        print ("Saindo ...")
        sys.exit(0)
    
if __name__ == "__main__": #Como se fosse um main
    m = Menu()
    m.executar()