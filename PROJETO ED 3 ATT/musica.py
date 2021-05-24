class BinaryTreeException(Exception):
    def __init__(self, mensagem):
        super().__init__(self,mensagem)

class Musica:
    def __init__(self, id, nome_mus, ano, album):
        self._nome_mus = nome_mus 
        self._ano = ano
        self._album = album
        self._id = id
        self._esq = None
        self._dir = None
        self._height = 1

# Property/Setter
    @property
    def nome_mus(self):
        return self._nome_mus
    @nome_mus.setter
    def nome_mus(self, novo):
        self._nome_mus = novo
    
    @property
    def ano (self):
        return self._ano
    @ano.setter
    def ano(self, novo):
        self._ano = novo
    
    @property
    def album (self):
        return self._album
    @album.setter
    def album(self, novo):
        self._album = novo
    
    @property
    def id (self):
        return self._id
    @id.setter
    def id(self, novo):
        self._id = novo

    @property
    def height (self):
        return self._height
    @height.setter
    def height(self, novo):
        self._height = novo
        
    @property
    def esq (self):
        return self._esq
    @esq.setter
    def esq(self, novo):
        self._esq = novo

    @property
    def dir (self):
        return self._dir
    @dir.setter
    def dir(self, novo):    
        self._dir = novo

#STR
    def __str__(self):
        return f'-----------\nNome da música: {self._nome_mus}\nAno de lançamento: {self._ano}\nÁlbum: {self._album}\nID: {self._id}\n-----------'

#NOVA ARVORE
