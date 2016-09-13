class Menu:
    def __init__(self):
        self.blocodenotas = Bloco

def executar(self): #É executado eternamente apresentado o menu com as escolhas para selecionar uma opção
    while True: #Verdadeiro pra sempre
            self.apresentar_menu #mostra o metodo apresentar menu
            escolha = raw_input("escolha uma opcao: ") #Tipo um scanf no C
            acao = self.escolhas.get(stl(escolha)) #Get=Busca no dicionario, é um metodo do python
            if acao:
                acao()
            else:
                print ("{0} nao foi uma escolha valida.".format(escolha))
                
def imprimir_notas(self, nota=None):
    if not nota:
        nota = self.blocodenotas.notas #Deve ter uma lista para as notas
    for n in nota:
        print ("{0}: {1}\n{2}".format(n.id,n.titulo, n.texto))
        
def buscar_notas(self):
    filtro = raw_input("Digite o ID da nota: ")
    nota = self.blocodenotas.buscar(filtro)
    self.imprimir_notas(nota)