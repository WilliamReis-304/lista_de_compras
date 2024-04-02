from banco import *

def adicionar(a,b,c):
    produto.update({"nome":a})
    produto.update({"valor":b})
    produto.update({"quantidade":c})
    totalProdutos.append(produto["valor"]*produto["quantidade"])
    return produto

def modificar(a,b,c,d):
    carrinho[d][0]["nome"]=a
    carrinho[d][0]["valor"]=b
    carrinho[d][0]["quantidade"]=c
    carrinho[d][0]["total"]=b*c
    return carrinho[d][0]

def total():
    contador = 0
    for i in range(len(carrinho)):
        contador += carrinho[i][0]["total"]
    print("O total de compras é:",contador)

def loop(a):
    while True:
        if a == "S":
            return True
        elif a == "N":
            return False
        else:
            a = input("Escolha uma opção válida! S ou N\n").upper()