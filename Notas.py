class Notas:
    def __init__(self, id = 0, texto = 0, titulo = 0, data = 0, indice = 0 ):
        self.id = id
        self.texto = texto
        self.titulo = titulo
        self.data = data
        self.indice = indice
        
    def setId(self, id):
        self.id = id
        
    def setTexto(self, texto):
        self.texto = texto
    
    def setTitulo(self, titulo):
        self.titulo = titulo
    
    def setData(self, data):
        self.data = data
    
    def setIndice(self, indice):
        self.indice = indice
        
    def __str__(self):
        return ("Identificador %i nota %s"%(self.id, self.texto))
    