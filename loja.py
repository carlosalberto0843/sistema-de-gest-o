def produtos1(venda_produtos , carrinho):                    
    print(venda_produtos)
    compra = input('digite o ID do produto: ')
    if compra in venda_produtos:
                                carrinho[compra] = venda_produtos[compra]
                                venda_produtos.pop(compra)
                                print('item adicionado com sucesso')    
    else:
        print('algo deu errado, tente novamente')
    return venda_produtos , carrinho
                       
def produtos2(carrinho , agenda):
    print()           
    finalizar = input('digite o numero do ID do produto desejado: ')
    agendar = input('digite a data para a retirada: ')
    if finalizar in carrinho:
                                carrinho[finalizar]['RETIRADA'] = agendar
                                agenda[finalizar] = carrinho[finalizar]
                                carrinho.pop(finalizar)
                                print('produto comprado com sucesso')
    else:
        print('produto nao comprado')
    return carrinho , agenda

def produtos3(carrinho, venda_produtos):
    print(carrinho)
    remover = input('digite o ID do produto: ')
    if remover in carrinho:
                                venda_produtos[remover] = carrinho[remover]
                                carrinho.pop(remover)
                                print('produto removido com sucesso')                          
    else:
                                print('algo deu errado, tente novamente')
    return carrinho, venda_produtos

def animais1(carrinho_animal, venda_animal):
    print(venda_animal)
    com = input('digite o numero do animal: ')
    if com in venda_animal:
        carrinho_animal[com] = venda_animal[com]
        venda_animal.pop(com)
        print('item adicionado ao carrinho com sucesso')
    else:
        print('algo deu errado, item nao adicionado')
    return carrinho_animal, venda_animal    

def animais2(carrinho_animal , agenda):
    print(carrinho_animal)
    com2 = input('digite o numero do animal: ')
    busca = input('digite a data para a retirada: ')
    if com2 in carrinho_animal:
        carrinho_animal[com2]['RETIRADA'] = busca
        agenda[com2] = carrinho_animal[com2]
        print('item comprado com sucesso \n')                            
    else:
        print('algo deu errado, item nao adicionado')

    return carrinho_animal , agenda

def ANIMAIS3(carrinho_animal , venda_animal):
    print(carrinho_animal)
    com3 = input('digite o numero do animal: ')
    if com3 in carrinho_animal:
        venda_animal[com3] = carrinho_animal[com3]
        carrinho_animal.pop(com3)
        print('item removido do carrinho com sucesso')
    else:
        print('algo deu errado, item nao removido')
    return carrinho_animal , venda_animal

def agenda1(agenda , histoico):
    print(agenda)
    recebe = input('digite o ID do item coletado: ')
    if recebe in agenda:
        histoico[recebe] = agenda[recebe]
        agenda.pop(recebe)
        print('iten coletado')
    else:
        print('seu item nao foi considerado como coletado')
    return agenda , histoico
