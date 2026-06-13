def venda_animais2( venda_animal , estoque_animal):
    print(venda_animal)
    produto_v2 = input('digite o numero do produto: ')
    if produto_v2 in venda_animal:
        venda_animal[produto_v2].pop('VALOR', None)
        estoque_animal[produto_v2] = venda_animal[produto_v2]
        venda_animal.pop(produto_v2)
        print('produto removido com sucesso \n')
    else:
        print('produto nao removido \n')
    return venda_animal , estoque_animal

def venda_animais3(venda_animal):
    print(venda_animal)
    troca_venda2 = input('digite o numero do produto: ')
    if troca_venda2 in venda_animal:
        novo_preco_animal = float(input('digite o novo valor: '))
        venda_animal[troca_venda2]['VALOR'] = novo_preco_animal

        print('valor atualizado com sucesso \n')
    else:
        print('algo deu errado \n')
    return venda_animal
