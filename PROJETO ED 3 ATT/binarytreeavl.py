from musica import BinaryTreeException, Musica

class AVL_Tree:

#MONTAR
    def add(self, root, key,nome_mus,ano,album): 
        if not root:
            return Musica(key, nome_mus, ano, album)
        elif key < root.id:
            root.esq = self.add(root.esq, key, nome_mus,ano,album)
        elif key > root.id:
            root.dir = self.add(root.dir,key, nome_mus,ano,album,)
        else:
            return root


        root.height = 1 + max(self.getHeight(root.esq), self.getHeight(root.dir))
 
        balance = self.getBalance(root)

        if balance > 1 and key < root.esq.id:
            return self.rotacaoDir(root)

        elif balance < -1 and key > root.dir.id:
            return self.rotacaoEsq(root)
 
        elif balance > 1 and key > root.esq.id:
            root.dir = self.rotacaoEsq(root.esq)
            return self.rotacaoDir(root)

        elif balance < -1 and key < root.dir.id:
            root.dir = self.rotacaoDir(root.dir)
            return self.rotacaoEsq(root)
 
        return root

#PROCURAR KEY    
    def findKey(self,root,key):
        if not root:
            print("O ID não foi encontrado.")
            return            
        if root.id > key:
            return self.findKey(root.esq,key)
        elif root.id < key:
            return self.findKey(root.dir,key)
        elif root.id == key:
            return print(root)          

#PROCURAR ANO
    def findAno(self, root, ano):
        if not root:
            return 
        self.findAno(root.esq,ano)
        self.findAno(root.dir, ano)
        if ano == root.ano:
            return print(root)
      
#ROTAÇÕES
    def rotacaoEsq(self, root):
        aux = root.dir
        T2 = aux.esq  
        aux.esq = root
        root.dir = T2

        root.height = 1 + max(self.getHeight(root.esq),
                         self.getHeight(root.dir))
        root.height = 1 + max(self.getHeight(aux.esq),
                         self.getHeight(aux.dir))
        return aux

    def rotacaoDir(self,root):
        aux = root.esq
        T3 = aux.dir
        aux.dir = root
        root.esq = T3
        
        root.height = 1 + max(self.getHeight(root.esq),
                        self.getHeight(root.dir))
        root.height = 1 + max(self.getHeight(aux.esq),
                        self.getHeight(aux.dir))
        return aux

#PRINT   
    def printTree(self, root):
        if not root:
            return

        self.printTree(root.esq)
        print(f"ID:{root.id}  Música: {root.nome_mus}  Lançamento: {root.ano}  Album: {root.album}")
        self.printTree(root.dir)
        
#ALTURA E BALANCIAMENTO ARVORE   
    def getHeight(self, root):
        if not root:
            return 0
        
        root.height = 1 + max(self.getHeight(root.esq), self.getHeight(root.dir))

        return root.height 
    
    def getBalance(self, node):
        if not node:
            raise BinaryTreeException("A árvore não existe")
        return self.getHeight(node.esq) - self.getHeight(node.dir)

#ORGANIZAR ORDEM ALFABETICA
    def ordCre(self,root):
        ordenar = []
        a = self._ordCre(root, ordenar)
        return a

    def _ordCre(self,root, ordenar):
        if not root:
            return
        if root is not None:
            self._ordCre(root.esq,ordenar)
            ordenar.append(root.nome_mus)
            self._ordCre(root.dir,ordenar)
        
        ordenado = (self.bubble_sort(ordenar))
        return ordenado

    def bubble_sort(self,lista):
        elementos = len(lista)-1
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(elementos):
                if lista[i] > lista[i+1]:
                    lista[i], lista[i+1] = lista[i+1],lista[i]
                    ordenado = False       
        return lista

#DISPLAY
    def display(self, root):
        if not None:
            print (root.id, root.height)
            if root.esq is not None:
                self.display(root.esq)
            if root.dir is not None:
                self.display(root.dir)


