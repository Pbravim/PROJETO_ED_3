from musica import Musica
from binarytreeavl import AVL_Tree

tree = AVL_Tree()
root = None
30,40,10,25,15
root = tree.add(root,30,"nome_mus",123,"album")
root = tree.add(root,40,"nome_mus",123,"album")
root = tree.add(root,10,"nome_mus",123,"album")
root = tree.add(root,25,"nome_mus",132,"album")
root = tree.add(root,15,"nome_mus",123,"album")

resposta = 0
lista_resposta = [1,2,3,4,5,6,7]
while resposta != 7:
    resposta = int (input("\nDigite: \n(1) Inserir música\n(2) Buscar música pelo id\n(3) Buscar músicas pelo ano\n(4) Listar músicas em ordem alfabética\n(5) Altura da árvore\n(6) Exibir a árvore\n(7) Sair do programa.\n "))
    
    if resposta == 1:
        nome_mus = str(input("Digite o nome da música: "))
        ano = int(input("Digite o ano de lançamento: "))
        album = str(input("Digite o álbum: "))
        id = int(input("Digite o ID: "))
        root = tree.add(root,id,nome_mus,ano,album)
        print(f"Foi adicionada a música {nome_mus}, lançada em {ano}, do álbum {album}, com o ID:{id}")

    elif resposta == 2:
        id = int(input("Digite o ID que deseja buscar: "))
        tree.findKey(root,id)

    elif resposta ==3:
        ano = int(input("Digite o ano em números: "))
        tree.findAno(root,ano)

    elif resposta ==4:
        a = tree.ordCre(root)
        print(f"Nomes em ordem crescente: {a}")
    
    elif resposta ==5:
        print(tree.getHeight(root))
                
    elif resposta ==6:
        tree.display(root)
