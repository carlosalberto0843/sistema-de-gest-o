def venda2(venda_produtos, estoque_produtos):
    print(venda_produtos)
    produto_v = input('digite o numero do produto: ')
    if produto_v in venda_produtos:
        venda_produtos[produto_v].pop('VALOR')
        estoque_produtos[produto_v] = venda_produtos[produto_v]
        venda_produtos.pop(produto_v)
        print('produto removido com sucesso \n')
    else:
        print('produto nao removido \n')
    return venda_produtos, estoque_produtos

def venda3(venda_produtos):
    print(venda_produtos)
    troca_venda = input('digite o numero do produto: ')
    if troca_venda in venda_produtos:
        novo_preco_produto = float(input('digite o novo valor: '))
        venda_produtos[troca_venda]['VALOR'] = novo_preco_produto
        print('valor atualizado com sucesso \n')
    else:
        print('algo deu errado \n')
    return venda_produtos