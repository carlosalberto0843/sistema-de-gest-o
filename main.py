from menu import *
from rebanho import *
from derivados import *
from derivados import opcao1_2
from login import *
from loja import *
from venda_produtos import *
from  venda_animais import *
adm = dict()
clientes = dict()
animal = dict()
animal_lactacao = dict()
produzido_lactaçao = dict()
estoque_animal = dict()
estoque_produtos = dict()
venda_animal = dict()
venda_produtos = dict()
carrinho = dict()
carrinho_animal = dict()
agenda = dict()
histoico = dict()
op = -99
noticia = "sem noticia hoje"

while op != 0:
    menu_principal()
    op = input('digite numero: ')
    if op == '1':    
        login_clientes(clientes)
    elif op == '2':
        login_adm(adm)

    elif op == '4':
        login = input('digite o nome de usuario: ')
        senha = input('digite a senha: ')       
        if login in adm and adm[login] == senha:
                    while True:   
                        menu(login)
                        geral = input('escolha a opçao: ')
                        if geral == '0':
                            print('')                        
                            print('ate mais')
                            print('')
                            break

                        elif geral == '3':
                            print('==CRIE UMA NOTICIA OU UM AVISO PARA OS COMPRADORES==')
                            noticia = input('digite a noticia: ')
                        
                        elif geral == '1':
                            print('---gerenciar rebanho---')
                            print('----------------------------------------------------')
                            print('Cadastrar animal - [1]')
                            print('buscar - [2]')
                            print('atualizar - [3]')
                            print('remover animais em lactaçao - [4]')
                            print('remover animais em engorda - [5]')
                            print('----------------------------------------------------')
                            gr = input('escolha a sua opçao: ')
                            if gr == '1':
                                opcao1(animal, animal_lactacao, estoque_animal)
                            elif gr == '2':
                                opcao2(animal, animal_lactacao, estoque_animal,venda_animal)
                            elif gr == '3':
                                opcao3(animal, animal_lactacao, estoque_animal)
                            elif gr == '4':
                                opcao4(animal_lactacao)
                            elif gr == '5':
                                opcao5(animal)
                            else:
                                print('numero invalido \n')
               

                        elif geral == '2':
                            print('----gerenciar producao e derivados----')
                            print('----------------------------------------------------')
                            print('gerenciar produçao diaria - [1]')
                            print('gerenciar estoque de animal  - [2]')
                            print('gerenciar estoque de produtos - [3]')
                            print('gerenciar itens para a venda - [4]')
                            print('voltar - [0]')
                            print('----------------------------------------------------')
                            escolha = input('selecione uma opcao: ')
                            if escolha == '1':
                                print('----GERENCIAR PRODUÇAO DIARIA----')
                                print('----------------------------------------------------')
                                print('cadastar produçao diaria - [1]')
                                print('ver produçao diaria de um animal - [2]')
                                print('remover item - [3]')
                                print('por para a venda - [4]')
                                print('----------------------------------------------------')
                                diaria = input('escolha uma opçao: ')
                                if diaria == '1':
                                   opcao1_2(animal_lactacao , produzido_lactaçao)                               
                                elif diaria == '4':
                                    opcao1_4(produzido_lactaçao)                                
                                elif diaria == '2':
                                    print(produzido_lactaçao)
                                elif diaria == '3':
                                    opcao1_3(produzido_lactaçao)                                
                                else:
                                    print('algo deu errado')        

                            elif escolha == '2':
                                print('----gerenciar estoque de animal----')
                                print('----------------------------------------------------')
                                print('ver animais em estoque - [1]')
                                print('remover animais do estoque - [2]')
                                print('inserir animal a venda -[3]')
                                print('voltar - [0]')
                                print('----------------------------------------------------')
                                escolha_animal = input('digite a opcao desejada: ')
                                if escolha_animal == '1':
                                    print(estoque_animal)
                                    print('')

                                elif escolha_animal == '2':
                                    print(estoque_animal)
                                    remov = input('digite o numero do animal desejado: ')
                                    if remov in estoque_animal:
                                        estoque_animal.pop(remov)
                                        print('animal removido com sucesso \n')
                                    else:
                                        print('animal nao removido, tente novamente \n')       

                                elif escolha_animal == '3':
                                    print(estoque_animal)
                                    remov2 = input('digite o numero do animal desejado: ')
                                    if remov2 in estoque_animal:
                                        preco2 = float(input('digite o valor: '))
                                        estoque_animal[remov2]['VALOR'] =  preco2
                                        venda_animal[remov2] = estoque_animal[remov2] 
                                        estoque_animal.pop(remov2)
                                        print('animal a venda com sucesso')
                                    else:
                                        print('animal nao adicionado, digite o numero novamente')
                                else:
                                    print('algo deu errado')
                            
                            elif escolha == '3':
                                print('----gerenciar estoque de produtos----') #gerenciar estoque de produtos
                                print('----------------------------------------------------')
                                print('ver protutos no estoque atual - [1]')
                                print('adicionar protudos ao estoque - [2]')
                                print('remover produtos do estoque - [3]')
                                print('colocar protutos a venda - [4]')
                                print('voltar - [5]')
                                print('----------------------------------------------------')
                                escolha_protudos = input('digite a opcao desejada: ')
                                if escolha_protudos == '1':
                                    print(estoque_produtos)
                                    print('')

                                elif escolha_protudos == '2':
                                    pro1 = input('digite o nome do produto: ')
                                    pro2 = float(input('digite a quantidade desse produto em kg ou litros: '))
                                    pro3 = input('digite a data de hoje: ')
                                    pro4 = input('digite numero para a indentificaçao: ')
                                    estoque_produtos[pro4] = { 'ID':pro4, 'NOME':pro1, 'QUANTIDADE':pro2 , 'EXP':pro3}
                                    print('produto adicionado \n')
                                
                                elif escolha_protudos == '3':
                                    print(estoque_produtos)
                                    remo = input('digite o numero do produto: ')
                                    if remo in estoque_produtos:
                                        estoque_produtos.pop(remo)
                                        print('produto removido com sucesso \n')

                                    else:
                                        print('produto nao removido, digite novamente')
                                        print('')

                                elif escolha_protudos == '4':
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
                                else:
                                    print('algo deu errado')
                            
                            elif escolha == '4':
                                print('----LISTA DE VENDAS----')
                                print('----------------------------------------------------')
                                print('vendas de animais - [1] ')
                                print('vendas de produtos - [2]')
                                print('----------------------------------------------------')
                                vender = input('digite a opcao: ')
                                if vender == '1':
                                    print('----VENDA ANIMAL----')
                                    print('----------------------------------------------------')  
                                    print('ver animais a venda - [1]')
                                    print('remover animal da venda - [2]')
                                    print('mudar preço de animal da venda - [3]')
                                    print('----------------------------------------------------')
                                    animais_venda = input('digite a opcao desejada: ')
                                    if animais_venda == '1':
                                        print(venda_animal ,'\n')                                    
                                    elif animais_venda == '2':
                                        venda_animais2( venda_animal , estoque_animal)                                    
                                    elif animais_venda == '3':
                                        venda_animais3(venda_animal)
                                    else:
                                        print('numero invalido, digite novamente \n')

                                elif vender == '2':
                                    print('----VENDA PRODUTOS----')
                                    print('----------------------------------------------------')  
                                    print('ver itens a venda - [1]')
                                    print('remover itens da venda - [2]')
                                    print('mudar preço de itens da venda - [3]')
                                    print('----------------------------------------------------')
                                    produto_venda = input('digite a opcao desejada: ')
                                    if produto_venda == '1':
                                        print(venda_produtos)                                   
                                    elif produto_venda == '2':
                                        venda2(venda_produtos, estoque_produtos)                                    
                                    elif produto_venda == '3':
                                        venda3(venda_produtos)
                                    else:
                                        print('algo deu errado')        
                            else:
                                print('algo deu errado')
        else:
                    print('As informações de login ou senha que você inseriu estão incorretas') 
                    print()              
    elif op == '3':
        login = input('digite o nome de usuario: ')
        senha = input('digite a senha: ')
        
        if login in clientes and clientes[login] == senha:
                while True:
                    print(f'--BEM VINDO {login.upper()}, OQUE DEJA COMPRAR HOJE--') 
                    print('-------------------------------------------------')
                    print('comprar produtos - 1')
                    print('comprar animais - 2')
                    print('ver itens agendados - 3')
                    print('logout - 0')
                    print('-------------------------------------------------')
                    print('NOTICIA OU AVISO DE HOJE: ', noticia.upper())
                    comprar = input('digite o item desejado: ')
                    if comprar == '0':
                        print('')                        
                        print('ate mais')
                        print('')
                        break                    
                    elif comprar == '1':
                        print('--LOJA DE PRODUTOS--')
                        print('----------------------------------------------------')
                        print('adicionar produtos ao carrinho - 1')
                        print('comprar itens do carrinho - 2')
                        print('remover items do carrinho - 3')
                        print('ver carrinho - 4')
                        print('sair - 0')
                        print('----------------------------------------------------')
                        loja = input('digite uma opçao: ')
                        if loja == '1':
                            produtos1(venda_produtos , carrinho)                    
                        elif loja == "4":
                            print(carrinho)
                        elif loja == '2':
                            produtos2(carrinho , agenda)                        
                        elif loja == '3':
                            produtos3(carrinho, venda_produtos)                        
                        else:
                            print('algo deu errado')              

                    elif comprar == '3':
                        print('--ITENS AGENDADOS--')
                        print('----------------------------------------------------')
                        print('ver itens agendados - [1]')
                        print('colocar iten como recebido - [2]')
                        print('ver itens ja coletados - [3]')
                        print('sair - [0]')
                        print('----------------------------------------------------')
                        coletar = input('digite uma opçao: ')
                        if coletar == '1':
                            print(agenda)
                        elif coletar == "2":
                            agenda1(agenda , histoico)
                        elif coletar == '3':
                            print(histoico)

                    elif comprar == '2':
                        print('--LOJA DE ANIMAIS--')
                        print('----------------------------------------------------')
                        print('adicionar animais ao carrinho - 1')
                        print('comprar animais do carrinho - 2')
                        print('remover animais do carrinho - 3')
                        print('ver carrinho - 4')
                        print('sair - 0')
                        print('----------------------------------------------------')
                        loja_animal = input('digite uma opçao: ')
                        if loja_animal == '1':
                            animais1(carrinho_animal, venda_animal)
                        elif loja_animal == '2':
                            animais2(carrinho_animal , agenda)                    
                        elif loja_animal == '3':
                            ANIMAIS3(carrinho_animal , venda_animal)
                        elif loja_animal == '4':
                            print(carrinho_animal)
                        else:
                            print('numero invalido, digite novamente')        
                    else:
                        print('numero invalido, digite novamente')                                           
        else:
            print('As informações de login ou senha que você inseriu estão incorretas')
    else:
        print('numero invalido, digite novamente')