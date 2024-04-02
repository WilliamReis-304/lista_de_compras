from banco import *
from funcoes import *
info = ["1","2","3","4","5"]

escolha = {
    "1":"Adicionar produto",
    "2":"Ver a lista de produtos",
    "3":"Atualizar lista de produtos",
    "4":"Remover Produto",
    "5":"Encerrar o Programa"
}
reiniciar = True

#Escolha das opções --------------------------------
while reiniciar == True:
    print("Escolha uma opção:\n")
    resposta = input(f"1 - {escolha['1']}\n2 - {escolha['2']}\n3 - {escolha['3']}\n4 - {escolha['4']}\n5 - {escolha['5']}\n")
    if resposta == "1":
        nome = input("Digite o nome do produto:\n")
        valor = float(input("Digite o preço do produto:\n"))
        quantidade = int(input("Digite a quantidade do produto:\n"))
        carrinho.append([adicionar(nome,valor,quantidade)])
        totalProdutos.append([adicionar(total)])
        print(f"produto adicionado:\n{carrinho}\n")
        print("O total de compras é:",sum(totalProdutos))
        decisao = input("há mais algo que deseja?(S/N)\n").upper()
        reiniciar = loop(decisao)
    elif resposta == "2":
        print(carrinho)
        print("O total de compras é:",sum(totalProdutos))
        decisao = input("há mais algo que deseja?(S/N)\n").upper()
        reiniciar = loop(decisao)
    elif resposta == "3":
        if len(carrinho) == 0:
            print("não há produtos no carrinho\n")
            continue
        else:
            busca = input("Digite o nome do produto que deseja modificar:\n")
            for i in range(len(carrinho)):
                if busca == carrinho[i][0]["nome"]:
                    nome = input("Digite o nome do produto:\n")
                    valor = float(input("Digite o preço do produto:\n"))
                    quantidade = int(input("Digite a quantidade do produto:\n"))
                    modificar(nome,valor,quantidade,i)
                    print("produto modificado:\n",carrinho)
                    print("O total de compras é:",sum(totalProdutos))
                    decisao = input("há mais algo que deseja?(S/N)\n").upper()
                    reiniciar = loop(decisao)
    elif resposta == "4":
        if len(carrinho) == 0:
            print("não há produtos no carrinho\n")
            continue
        else:
            busca = input("Digite o nome do produto que deseja remover:\n")
            for i in range(len(carrinho)):
                if busca == carrinho[i][0]["nome"]:
                    carrinho.pop(i)
                    print("produto removido:\n",carrinho)
                    print("O total de compras é:",sum(totalProdutos))
                    decisao = input("há mais algo que deseja?(S/N)\n").upper()
                    reiniciar = loop(decisao)
    elif resposta == "5":
        break
print("Volte sempre!")