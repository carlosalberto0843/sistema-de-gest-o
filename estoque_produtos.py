def estoque1(estoque_produtos):
    pro1 = input('digite o nome do produto: ')
    pro2 = float(input('digite a quantidade desse produto em kg ou litros: '))
    pro3 = input('digite a data de hoje: ')
    pro4 = input('digite numero para a indentificaçao: ')
    estoque_produtos[pro4] = { 'ID':pro4, 'NOME':pro1, 'QUANTIDADE':pro2 , 'EXP':pro3}
    print('produto adicionado \n')
    return estoque_produtos

def estoque2(estoque_produtos):
    print(estoque_produtos)
    remo = input('digite o numero do produto: ')
    if remo in estoque_produtos:
        estoque_produtos.pop(remo)
        print('produto removido com sucesso \n')

    else:
        print('produto nao removido, digite novamente')
    return estoque_produtos

def estoque3(estoque_produtos , venda_produtos):
    print(estoque_produtos)
    colocar_venda = input('digite o numero do produto: ')
    if colocar_venda in estoque_produtos:
        preco = float(input('digite o preco: '))
        estoque_produtos[colocar_venda] = {'VALOR':preco}
        venda_produtos[colocar_venda] = estoque_produtos[colocar_venda]
        print('produto adicionado com sucesso \n')
    else:
        print('produto nao inserido')
        print('')
    return estoque_produtos , venda_produtos