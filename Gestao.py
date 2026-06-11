
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
    print('----BEM VINDO AO SISTEMA DE GESTAO AGROPECUARIA----')
    print('----------------------------------------------------')
    print('cadastrar cliente - 1:')
    print('cadastrar ADM - 2:')
    print('login cliente - 3')
    print('login ADM - 4')
    print('----------------------------------------------------')
    op = input('digite numero: ')

    if op == '1':
        nome = input('digite seu nome: ')
        senha = input('digite sua senha: ')
        clientes.append([nome , senha])
        print('conta criada em cliente')

    elif op == '2':
        nome2 = input('digite seu nome: ')
        senha2 = input('digite sua senha: ')
        if nome2 in adm:
            print('nome do usuario ja existente, digite outro nome \n')
        else:
            adm[nome2] = senha2
            print('conta criada em adm')

    elif op == '4': #LOGIN #nao esquecer do else no final

        login = input('digite o nome de usuario: ')
        senha = input('digite a senha: ')       
        
        if login in adm and adm[login] == senha:
                    while True:   
                        print(f'SEJA BEM VINDO {login.upper()}')                                   
                        print('----MENU DO ADM----')
                        print('----------------------------------------------------')
                        print('Gerenciar Rebanho - [1]')
                        print('gerenciar producao e derivados - [2]')
                        print('criar noticia ou aviso - [3]')
                        print('listar todos os itens - [4]')
                        print('logout - [0]')
                        print('----------------------------------------------------')
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
                            print('atualizar status - [3]')
                            print('atualizar animal - [4]')
                            print('remover animais em lactaçao - [5]')
                            print('remover animais em engorda - [6]')
                            print('----------------------------------------------------')
                            gr = input('escolha a sua opçao: ')
                            if gr == '1':
                                l2 = input('digite o tipo de animal: ')
                                l4 = float(input('digite o peso em kg do animal: '))
                                l1 = input('digite a identificaçao do animal - [brinco/número]: ')
                                l3 = input('digite o status do animal - [lactacao, engorda, venda]: ')
                                if l3 == 'engorda':
                                    animal[l1] = {'brinco': l1, 'tipo': l2, 'status': l3, 'peso': l4}
                                    print('animal adicionado')

                                elif l3 == 'lactacao':
                                    animal_lactacao[l1] = {'brinco': l1, 'tipo': l2, 'status': l3, 'peso': l4}
                                    print('animal adicionado')
                                
                                elif l3 == 'venda':
                                    estoque_animal[l1] = {'brinco': l1, 'tipo': l2, 'status': l3, 'peso': l4}
                                    print('animal adcionado')

                            elif gr == '2':
                                print('animais em lactaçao')
                                print(animal_lactacao, '\n')
                                print('animais para engorda')
                                print(animal, '\n')
                                print('animais em estoque')
                                print(estoque_animal,'\n')
                                print('animais postos á venda')  
                                print(venda_animal ,'\n')      

                            elif gr == '3': 
                                mudar = input('o animal desejado é de lactaçao, engorda ou venda: ')
                                atualizar = input('deseja mudar para lactaçao, engorda ou venda: ')
                                num = input('digite o numero do animal: ')
                                
                                if mudar == 'lactacao' and atualizar == 'engorda':
                                    animal_lactacao[num]['status'] = 'engorda'
                                    animal[num] = animal_lactacao[num]
                                    animal_lactacao.pop(num)
   
                                elif mudar == 'lactacao' and atualizar == 'venda':
                                     animal_lactacao[num]['status'] = 'venda'
                                     estoque_animal[num] = animal_lactacao[num]
                                     animal_lactacao.pop(num)


                                elif mudar == 'venda' and atualizar == 'lactacao':
                                    estoque_animal[num]['status'] = 'lactacao'
                                    animal_lactacao[num] = estoque_animal[num]
                                    estoque_animal.pop(num)

                                elif mudar == 'venda' and atualizar == 'engorda':
                                    estoque_animal[num]['status'] = 'engorda'
                                    animal[num] = estoque_animal[num]
                                    estoque_animal.pop(num)


                                elif mudar == 'engorda' and atualizar == 'lactacao':
                                    animal[num]['status'] = 'lactacao'
                                    animal_lactacao[num] = animal[num]
                                    animal.pop(num)

                                elif mudar == 'engorda' and atualizar == 'venda':
                                    animal[num]['status'] = 'venda'
                                    estoque_animal[num] = animal[num]
                                    animal.pop(num)
                                
                                else:
                                    print('algo deu errado \n')

                            elif gr == '4':
                                troca = input('qual o status do seu animal: ')
                                if troca == 'lactacao':
                                    print(animal_lactacao)
                                    animal2 = input('digite o numero do animal: ')
                                    valor = input('digite o item que deseja alterar: ')
                                    novo_valor = input('digie o novo valor: ')
                                    animal_lactacao[animal2][valor] = novo_valor

                            elif gr == '5':
                                print(animal_lactacao)
                                nu5 = input('digite o numero do animal: ')
                                if nu5 in animal_lactacao:
                                    animal_lactacao.pop(nu5)   
                                    print('animal removido de lactaçao')
                                else:
                                    print('animal nao removido')
                                
                            elif gr == '6':
                                print(animal)
                                nu5 = input('digite o numero do animal: ')
                                if nu5 in animal:
                                    animal.pop(nu5)   
                                    print('animal removido de engorda')
                                else:
                                    print('animal nao removido')        
                            else:
                                print('algo deu errado')                

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
                                    colocar = input('digite o numero do animal em lactaçao:')
                                    
                                    if colocar in animal_lactacao:        
                                        print(animal_lactacao[colocar])
                                        ad2 = input('numero para identificaçao: ')
                                        ad = float(input('quantos litros de leite foi produzido por esse animal: '))
                                        ad1 = input('data de expediçao do leite: ')
                                        produzido_lactaçao[ad2] = {'ANIMAL':colocar, 'ID':ad2, 'LITROS':ad , 'EXP':ad1,}
                                        print('produto adicionado')
                                    else:
                                        print('produto nao adicionado')

                                elif diaria == '4':
                                    for i in produzido_lactaçao:
                                        print(i)
                                    print()
                                    por_venda = input('digite o id do produto para o venda: ')
                                    index = -1
                                    for i in range(len(produzido_lactaçao)):
                                        if produzido_lactaçao[i][1] == por_venda:
                                            index = i
                                    if index >= 0:
                                        venda_produtos.append[index]
                                        print('produto inserido a venda')

                                    else:
                                        print('produto nao inserido, algo deu errado')

                                elif diaria == '2':
                                    colocar2 = input('digite o numero do animal: ')
                                    soma = 0
                                    for i in range(len(produzido_lactaçao)):
                                        if produzido_lactaçao[i][0] == colocar2:
                                            soma = soma + produzido_lactaçao[i][2]
                                            print(produzido_lactaçao[i])
                                    print(f'esse animal produziu ao todo {soma}')
                                    print('')

                                elif diaria == '3':
                                    pro = input('digite o numero de indendificaçao da diaria: ')
                                    index = -1
                                    for l in range(len(produzido_lactaçao)):
                                        if produzido_lactaçao[l][1] == pro:
                                            index = l
                                    if index >= 0:
                                        produzido_lactaçao.pop(index)
                                        print('iten removido')
                                        print()
                                    else:
                                        print('iten nao removido')
                                        print()
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
                                    for itens in estoque_animal:
                                        print(itens)
                                    print('')

                                elif escolha_animal == '2':
                                    for i in estoque_animal:
                                        print(i)
                                    nu_ani = input('digite o numero do animal: ')
                                    index = -1
                                    for ita in range(len(estoque_animal)):
                                        if estoque_animal[i][0] == nu_ani:
                                            index = i
                                            break
                                    if index >= 0:
                                        estoque_animal.pop(index)  
                                        print('animal removido com sucesso')
                                    else:
                                        print('animal nao removido, tente novamente')       

                                elif escolha_animal == '3':
                                    print(escolha_animal)
                                    nu = input('digite numero do animal: ')
                                    dinheiro = float(input('digite o valor do animal para venda: '))
                                    achei = -1
                                    for ites in range(len(estoque_animal)):
                                        if estoque_animal[ites][0] == nu:  
                                            index = ites

                                    if index >= 0:
                                        estoque_animal[ites][4] = dinheiro
                                        venda_animal.append(estoque_animal[index])
                                        estoque_animal.pop(index)
                                        print('animal adicionado a venda')

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
                                    for itens in estoque_produtos:
                                        print(itens)
                                    print('')

                                elif escolha_protudos == '2':
                                    pro1 = input('digite o nome do produto: ')
                                    pro2 = float(input('digite a quantidade desse produto em kg ou litros: '))
                                    pro3 = input('digite a data de hoje: ')
                                    pro4 = input('digite numero para a indentificaçao: ')
                                    estoque_produtos.append([pro4, pro1, pro2 ,pro3, '' , ''])
                                
                                elif escolha_protudos == '3':
                                    print(estoque_produtos)
                                    remo = input('digite o numero do produto: ')
                                    for i in range(len(estoque_produtos)):
                                        if estoque_produtos[i][0] in remo:
                                            index = -1
                                    if index >= 0:
                                        estoque_produtos.pop(index)
                                        print('produto removido com sucesso')
                                        print('')
                                    else:
                                        print('produto nao removido, digite novamente')
                                        print('')

                                elif escolha_protudos == '4':
                                    colocar_venda = input('digite o numero do produto: ')
                                    index = -1
                                    for i in range(len(estoque_produtos)):
                                        if estoque_produtos[i][0] == colocar_venda:
                                            index = i
                                            break
                                    
                                    if index >= 0:
                                        preco = float(input('digite o valor do produto: '))
                                        estoque_produtos[index][4] = preco
                                        venda_produtos.append(estoque_produtos[index])
                                        estoque_produtos.pop(index)
                                        print('produto inserido para venda')
                                        print('')
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
                                    print('ver animal a venda - [1]')
                                    print('remover animal da venda - [2]')
                                    print('mudar preço de animal da venda - [3]')
                                    print('----------------------------------------------------')
                                    animais_venda = input('digite a opcao desejada: ')
                                    if animais_venda == '1':
                                        soma = 0
                                        print('')
                                        print('-NUM ID-  -TIPO ANI-  -STATUS-  -PESO-  -VALOR R$-')
                                        for f in range(len(venda_animal)):
                                            print(venda_animal[f])
                                            soma = soma + venda_animal[f][4]
                                        
                                        print(f'o valor dos animais em total é R$: {soma}')
                                        print('')

                                    elif animais_venda == '2':
                                        nu_animal = input('digite o numero do animal: ')
                                        index = -1
                                        for g in range(len(venda_animal)):
                                            if venda_animal[g][0] == nu_animal:
                                                index = g
                                                break
                                        if index >= 0:
                                            venda_animal[index][4] == []
                                            estoque_animal.append(venda_animal[index])
                                            venda_animal.pop(index)
                                            print('animal removido da venda, esse animal retornou ao estoque')
                                            print('')
                                        else:
                                            print('animal nao removido')
                                            print('')

                                    elif animais_venda == '3':
                                        troca_nu = input('digite o numero do animal: ')
                                        index = -1
                                        for g in range(len(venda_animal)):
                                            if venda_animal[g][0] in troca_nu:
                                                index = g
                                                break
                                        if index >= 0:
                                            novo_preco_animal = float(input('digite o novo preço em R$: '))
                                            venda_animal[index][4] = novo_preco_animal
                                            print('preço atualizado')
                                            print('')
                                        else:
                                            print('preço nao alterado')
                                            print('') 

                                elif vender == '2':
                                    print('----VENDA PRODUTOS----')
                                    print('----------------------------------------------------')  
                                    print('ver itens a venda - [1]')
                                    print('remover itens da venda - [2]')
                                    print('mudar preço de itens da venda - [3]')
                                    print('----------------------------------------------------')
                                    produto_venda = input('digite a opcao desejada: ')
                                    if produto_venda == '1':
                                        soma = 0
                                        print('')
                                        print('-NUM DE ID-  -TIPO-  -QUANTITADE-  -DATA EXP-  -VALOR R$-')
                                        for f in range(len(venda_produtos)):
                                            print(venda_produtos[f])
                                            soma = soma + venda_produtos[f][4]
                                        
                                        print(f'o valor total a venda é de R$: {soma}')
                                        print('') 
                                    
                                    elif produto_venda == '2':
                                        produto_v = input('digite o numero do produto: ')
                                        index = -1
                                        for i in range(len(venda_produtos)):
                                            if venda_produtos[i][0] == produto_v:
                                                index = i
                                                break
                                        if index >= 0:
                                            venda_produtos[index][4] = []
                                            estoque_produtos.append(venda_produtos[index])
                                            venda_produtos.pop(index)
                                            print('produto removido da venda, esse produto retornou ao seu estoque')
                                            print('')
                                        else:
                                            print('produto nao removido')
                                            print('')
                                    
                                    elif produto_venda == '3':
                                        troca_venda = input('digite o numero do produto: ')
                                        index = -1
                                        for i in range(len(venda_produtos)):
                                            if venda_produtos[i][0] in troca_venda:
                                                index = i
                                                break
                                        if index >= 0:
                                            novo_preco = float(input('digite o novo preço: '))
                                            venda_produtos[index][4] = novo_preco
                                            print('novo preço atualizado')
                                            print('')                                    
                                        else:
                                            print('algo deu errado')
                                            print()
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
                            print('-NUM DE ID-  -TIPO-  -QUANTITADE-  -DATA EXP-  -VALOR R$-')
                            for i in venda_produtos:
                                print(i)
                            comprado = input('digite o numero do ID do produto desejado: ')
                            index = -1
                            for p in range(len(venda_produtos)):
                                if venda_produtos[p][0] == comprado:
                                    index = p
                                    break
                            if index >= 0:
                                carrinho.append(venda_produtos[index])
                                venda_produtos.pop(index)
                                print('item adicionado com sucesso')    
                            else:
                                print('algo deu errado, tente novamente')
                        elif loja == "4":
                            for i in carrinho:
                                print(i)
                            print()        

                        elif loja == '2':
                            for i in carrinho:
                                print(i)
                            index = -1
                            finalizar = input('digite o numero do ID do produto desejado: ')
                            agendar = input('digite a data para a retirada: ')
                            for i in range(len(carrinho)):
                                if carrinho[i][0] == finalizar:
                                    index = i
                                    break
                            if index >= 0:
                                carrinho[index][5] = agendar
                                agenda.append(carrinho[index])
                                carrinho.pop(index)
                                print('produto comprado com sucesso')
                            else:
                                print('produto nao comprado')

                        elif loja == '3':
                            print('-NUM DE ID-  -TIPO-  -QUANTITADE-  -DATA EXP-  -VALOR R$-')
                            for i in carrinho:
                                print(i)
                            print()
                            index = -1    
                            remover = input('digite o numero do ID do produto desejado: ')
                            for h in range(len(carrinho)):
                                if carrinho[p][0] == remover:
                                    index = h
                                    break
                            if index >= 0:
                                    venda_produtos.append(carrinho[index])
                                    carrinho.pop(index)
                                    print('produto removido com sucesso')
                            else:
                                print('algo deu errado, tente novamente') 
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
                            for i in agenda:
                                print(i)
                            print()

                        elif coletar == "2":
                            for i in agenda:
                                print(i)
                            print()
                            index = -1
                            recebe = input('digite o ID do item coletado: ')
                            for b in range(len(agenda)):
                                if agenda[b][0] == recebe:
                                    index = b
                            if index >= 0:
                                histoico.append(agenda[index])
                                agenda.pop(index)
                                print('iten coletado')
                            else:
                                print('seu item nao foi considerado como coletado')

                        elif coletar == '3':
                            for i in histoico:
                                print(i)
                            print()

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
                            print('-NUM ID-  -TIPO ANI-  -STATUS-  -PESO-  -VALOR R$-')
                            for i in venda_animal:
                                print(i)
                            print()
                            com = input('digite o numero do animal: ')
                            index = -1
                            for g in range(len(venda_animal)):
                                if venda_animal[g][0] == com:
                                    index = g
                            if index >= 0:
                                carrinho_animal.append(venda_animal[index])
                                print('item adicionado ao carrinho com sucesso')
                            else:
                                print('algo deu errado, item nao adicionado')                            

                        elif loja_animal == '2':
                            print('-NUM ID-  -TIPO ANI-  -STATUS-  -PESO-  -VALOR R$-')
                            for i in carrinho_animal:
                                print(i)
                            print()
                            com = input('digite o numero do animal: ')
                            busca = input('digite a data: ')
                            index = -1
                            for g in range(len(carrinho_animal)):
                                if carrinho_animal[g][0] == com:
                                    index = g
                            if index >= 0:
                                carrinho_animal[index][5] = busca
                                agenda.append(carrinho_animal[index])
                                print('item comprado com sucesso')
                            else:
                                print('algo deu errado, item nao adicionado')

                        elif loja_animal == '3':
                            print('-NUM ID-  -TIPO ANI-  -STATUS-  -PESO-  -VALOR R$-')
                            for i in carrinho_animal:
                                print(i)
                            print()
                            com = input('digite o numero do animal: ')
                            index = -1
                            for g in range(len(carrinho_animal)):
                                if carrinho_animal[g][0] == com:
                                    index = g
                            if index >= 0:
                                venda_animal.append(carrinho_animal[index])
                                carrinho_animal.pop(index)
                                print('item removido do carrinho com sucesso')
                            else:
                                print('algo deu errado, item nao removido')
                        else:
                            print('numero invalido, digite novamente')        
                    else:
                        print('numero invalido, digite novamente')                                           
        else:
            print('As informações de login ou senha que você inseriu estão incorretas')
    else:
        print('numero invalido, digite novamente')