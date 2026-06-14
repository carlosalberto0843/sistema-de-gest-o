def opcao1_1(animal_lactacao , produzido_lactaçao):
    colocar = input('digite o numero do animal em lactaçao:')                                
    if colocar in animal_lactacao:        
        ad2 = input('numero para identificaçao: ')
        ad = float(input('quantos litros de leite foi produzido por esse animal: '))
        ad1 = input('data de expediçao do leite: ')
        produzido_lactaçao[ad2] = {'ANIMAL':colocar, 'ID':ad2, 'LITROS':ad , 'EXP':ad1,} 
        print('produto adicionado \n')
    else:
        print('produto nao adicionado \n')
    return produzido_lactaçao

def opcao1_4(produzido_lactaçao, venda_produtos):
    print(produzido_lactaçao)
    print()
    animal = input('digite o numero do animal: ')
    por_venda = input('digite o produto a venda: ')
    if produzido_lactaçao[por_venda]['ID'] == animal:
        novo_preco = float(input('digite o valor desejado: '))
        produzido_lactaçao[por_venda]['VALOR'] = novo_preco
        produzido_lactaçao.pop('ANIMAL')
        venda_produtos[por_venda] = produzido_lactaçao[por_venda]
        produzido_lactaçao.pop(por_venda)
        print('preço atualizado \n')
    else:
        print('produto nao inserido, algo deu errado')
    return produzido_lactaçao, venda_produtos

def opcao1_2(produzido_lactaçao):
    colocar2 = input('digite o numero do animal: ')
    for brinco, dados in produzido_lactaçao.items():
        if dados['ANIMAL'] == colocar2:
            print(brinco, dados)

def opcao1_3(produzido_lactaçao):                                    
    pro = input('digite o numero de indendificaçao do animal: ')
    if pro in produzido_lactaçao:
        remover = input('digite o numero do ')
        produzido_lactaçao.pop(pro)
        print('produto removido \n')
    else:
        print('iten nao removido')
        print()
    return produzido_lactaçao


                             




