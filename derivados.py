def opcao1_2(animal_lactacao , produzido_lactaçao):
    colocar = input('digite o numero do animal em lactaçao:')                                
    if colocar in animal_lactacao:        
        print(produzido_lactaçao[colocar])
        ad2 = input('numero para identificaçao: ')
        ad = float(input('quantos litros de leite foi produzido por esse animal: '))
        ad1 = input('data de expediçao do leite: ')
        produzido_lactaçao[ad2] = {'ANIMAL':colocar, 'ID':ad2, 'LITROS':ad , 'EXP':ad1,}
        print('produto adicionado')
    else:
        print('produto nao adicionado')
    return produzido_lactaçao

def opcao1_4(produzido_lactaçao):
    print(produzido_lactaçao)
    print()
    por_venda = input('digite o produto a venda: ')
    if por_venda in produzido_lactaçao:
        novo_preco = float(input('digite o valor desejado: '))
        produzido_lactaçao[por_venda]['VALOR'] = novo_preco
        print('preço atualizado \n')
    else:
        print('produto nao inserido, algo deu errado')
    return produzido_lactaçao

def opcao1_3(produzido_lactaçao):
    colocar2 = input('digite o numero do animal: ')
    soma = 0
    brinco = input('Digite o número do brinco: ')
    for chave, dados in produzido_lactaçao.items():
        if dados['BRINCO'] == brinco:
            print('Animal encontrado:')
            print(dados)
            break
        else:
            print('Animal não encontrado.')
            print(produzido_lactaçao)
            print(f'esse animal produziu ao todo {soma} \n')

def opcao1_4(produzido_lactaçao):                                    
    pro = input('digite o numero de indendificaçao da diaria: ')
    if pro in produzido_lactaçao:
        produzido_lactaçao.pop(pro)
        print('produto removido \n')
    else:
        print('iten nao removido')
        print()
    return produzido_lactaçao


                             




