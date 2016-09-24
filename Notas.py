class Notas:
    def __init__(self, id = 0, texto = 0, titulo = 0, data = 0, indice = 0 ):
        self.id = id
        self.texto = texto
        self.titulo = titulo
        self.data = data
        self.indice = indice
        
    def setNota(self, id, texto, titulo, data, indice):        
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
        return ("""
        Nota(s):
        %i: \n
        ID: %i \n
        Titulo: %s \n
        Texto: %s \n
        Data de Criacao: %s \n
        """%(self.indice, self.id, self.titulo, self.texto, self.data))
    