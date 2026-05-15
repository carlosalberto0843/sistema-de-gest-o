adm = []
clientes = []
animal = []
animal_lactacao = []
produzido_lactaçao = []
estoque_animal = []
estoque_produtos = []
venda_animal = []
venda_produtos = []
carrinho = []
agenda = []
histoico = []
op = -99
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
        adm.append([nome2 , senha2])
        print('conta criada em adm')
    
    elif op == '4': #LOGIN #nao esquecer do else no final

        login = input('diga a login: ')
        senha = input('diga a senha: ')       
        for a in adm:
                if login == a[0] and senha == a[1]:
                    while True:   
                        print(f'seja bem vindo {login}')                                   

                        print('----------------------------------------------------')
                        print('Gerenciar Rebanho - [1]')
                        print('gerenciar producao e derivados - [2]')
                        print('logout - [0]')
                        print('----------------------------------------------------')
                        geral = input('escolha a opçao: ')
                        if geral == '0':
                            print('')                        
                            print('ate mais')
                            print('')
                            break
                        elif geral == '1':
                            print('---gerenciar rebanho---')
                            print('----------------------------------------------------')
                            print('Cadastrar animal - [1]')
                            print('buscar - [2]')
                            print('atualizar - [3]')
                            print('remover animais em lactaçao - [4]')
                            print('----------------------------------------------------')
                            gr = input('escolha a sua opçao: ')
                            if gr == '1':
                                l1 = input('digite o tipo de animal: ')
                                l4 = float(input('digite o peso em kg do animal: '))
                                l2 = (input('digite a identificaçao do animal - [brinco/número]: '))
                                l3 = input('digite o status do animal - [lactacao, engorda, venda]: ')
                                if l3 == 'engorda':
                                    animal.append([l1, l2, l3, l4, []])
                                    print('animal adcionado')

                                elif l3 == 'lactacao':
                                    animal_lactacao.append([l1, l2, l3, l4 , []])
                                    print('animal adicionado')
                                
                                elif l3 == 'venda':
                                    estoque_animal.append([l1, l2, l3, l4, []])
                                    print('animal adcionado')

                            elif gr == '2':
                                buscar2 = input('digite o status do animal: ')
                                buscar = input('digite o numero do animal: ')
                                index = -1
                                if buscar2 == 'lactacao':
                                    for i in range(len(animal_lactacao)):
                                        if animal_lactacao[i] == buscar:
                                            index = i
                                            break
                                    if index >= 0:
                                        print(f'seu animal é {animal_lactacao[index]}')
                                    else:
                                        print('animal nao encontrado')
                                elif buscar2 == 'venda':
                                    for i in range(len(estoque_animal)):
                                        if estoque_animal[i] == buscar:
                                            index = i
                                            break
                                    if index >= 0:
                                        print(f'seu animal é {estoque_animal[index]}')
                                    else:
                                        print('animal nao encontrado')
                                        
                            elif gr == '3': 
                                print(f'animais em {animal}')
                                print(f'animais em {estoque_animal}')
                                mudar = input('o animal desejado é de lactaçao, engorda ou venda: ')
                                atualizar = input('deseja mudar para lactaçao, engorda ou venda: ')
                                num = input('digite o numero do animal: ')
                                
                                if mudar == 'engorda' and atualizar == 'venda':
                                    index = -1
                                    for troca in range(len(animal)):
                                        if animal[trocar][1] == num:
                                            index = trocar
                                    if index >= 0:        
                                        troca[2] = 'venda'
                                        estoque_animal.append(animal(troca))
                                        animal.remove(troca)
                                        print('animal atualizado')
                                        print()
                                    else:
                                        print('algo deu errado')
                                        print()    
   
                                elif  mudar == 'venda' and atualizar == 'lactaçao':
                                    index = -1
                                    for troca in range(len(estoque_animal)):
                                        if troca[1][1] == num:
                                            index = troca
                                    if index >= 0:
                                        troca[2] = 'lactaçao'
                                        animal.append(estoque_animal(index))
                                        estoque_animal.pop(troca)
                                        print('animal atualizado')
                                    else:
                                        print('algo deu errado')
                                        print() 

                                elif mudar == 'venda' and atualizar == 'engorda':
                                    for troca in estoque_animal:
                                        if troca[1] == num:
                                            troca[2] = 'engorda'
                                            animal.append(troca)
                                            estoque_animal.remove(troca)
                                            print('animal atualizado')
                                            trocar = True
                                            break

                            if gr == '4':
                                print(animal)
                                nu5 = input('digite o numero do animal: ')
                                achei = False
                                for im in animal:
                                    if im[1] == nu5:
                                        animal.remove(im)
                                        print('animal removido de lactaçao')
                                        achei = True
                                          
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
                                    index = -1
                                    for i in range(len(animal_lactacao)):
                                        if animal[i][1] == colocar:
                                            index = i
                                    if index >= 0:        
                                        print(animal_lactacao[index])
                                        ad2 = input('numero para identificaçao: ')
                                        ad = float(input('quantos litros de leite foi produzido por esse animal: '))
                                        ad1 = input('data de expediçao do leite: ')
                                        produzido_lactaçao.append([colocar, ad2, ad ,ad1])
                                        print('produto adicionado')
                                    else:
                                        print('produto nao adicionado')
                                        
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
                                        if estoque_animal[i][1] == nu_ani:
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
                                        if estoque_animal[ites][1] == nu:  
                                            index = ites

                                    if index >= 0:
                                        estoque_animal[ites][4] = dinheiro
                                        venda_animal.append(estoque_animal[index])
                                        estoque_animal.pop(index)
                                        print('animal adicionado a venda')

                                    else:
                                        print('animal nao adicionado, digite o numero novamente')

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
                                    estoque_produtos.append([pro4, pro1, pro2 ,pro3, []])
                                
                                elif escolha_protudos == '3':
                                    print(estoque_produtos)
                                    remo = input('digite o numero do produto: ')
                                    for i in range(len(estoque_produtos)):
                                        if estoque_produtos[i][0] in remo:
                                            index = -1
                                    if index >= 0:
                                        estoque_produtos.pop[index]
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

                            elif escolha == 4:
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
                                        print('-TIPO ANI-  -NUM ID-  -STATUS-  -PESO-  -VALOR R$-')
                                        for i in range(len(venda_animal)):
                                            print(venda_animal[f])
                                            soma = soma + venda_animal[f][4]
                                        
                                        print(f'o valor dos animais em total é R$: {soma}')
                                        print('')

                                    elif animais_venda == '2':
                                        nu_animal = input('digite o numero do animal: ')
                                        index = -1
                                        for g in range(len(venda_animal)):
                                            if venda_animal[g][1] == nu_animal:
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
                                            if venda_animal[g][1] in troca_nu:
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
                                            estoque_produtos.append(venda_produtos(index))
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
                                            print('')
    elif op == '3':
        login = input('diga a login: ')
        senha = input('diga a senha: ')
        bv = False
        for a in clientes:
            if login == a[0] and senha == a[1]:
                while True:
                    print(f'--BEM VINDO {login}, OQUE DEJA COMPRAR HOJE--') 
                    print('-------------------------------------------------')
                    print('comprar produtos - 1')
                    print('comprar animais - 2')
                    print('ver itens agendados - 3')
                    print('logout - 0')
                    print('-------------------------------------------------')
                    comprar = input('digite o item desejado: ')
                    if comprar == 0:
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
                        print('ver produtos comprados - 4')
                        print('sair - 0')
                        print('----------------------------------------------------')
                        loja = input('digite uma opçao: ')
                        if loja == 1:
                            print('-NUM DE ID-  -TIPO-  -QUANTITADE-  -DATA EXP-  -VALOR R$-')
                            for i in venda_produtos:
                                print(i)
                            comprado = input('digite o numero do ID do produto desejado: ')
                            index = -1
                            for p in range(len(venda_produtos)):
                                if venda_produtos[p][0] == comprado:
                                    index = p
                            if index >= 0:
                                carrinho.append(venda_produtos(index))
                                venda_produtos.pop(index)
                            else:
                                print('algo deu errado, tente novamente')

                        elif loja == '2':
                            print('-NUM DE ID-  -TIPO-  -QUANTITADE-  -DATA EXP-  -VALOR R$-')
                            for i in carrinho:
                                print(i)
                            index = -1
                            finalizar = input('digite o numero do ID do produto desejado: ')
                            agendar = input('digite a data')
                            for i in range(len(carrinho)):
                                if carrinho[i][0] == finalizar:
                                    index = i
                            if index >= 0:
                                venda_produtos[index][5] = agendar
                                agenda.append(venda_produtos(index))
                                venda_produtos.pop(index)
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
                            if index >= 0:
                                    carrinho.pop(index)
                                    print('produto removido com sucesso')
                            else:
                                print('algo deu errado, tente novamente')       
                        elif loja == '4':
                            for i in histoico:
                                print(i)
                            print()

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
                            print('-NUM DE ID-  -TIPO-  -QUANTITADE-  -DATA EXP-  -VALOR R$- -DATA DE RETIRADA-')
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
                                histoico.append(index)
                                agenda.pop(index)
                                print('iten coletado')
                            else:
                                print('seu item nao foi considerado como coletado')

                        elif coletar == '3':
                            print('-NUM DE ID-  -TIPO-  -QUANTITADE-  -DATA EXP-  -VALOR R$- -DATA DE RETIRADA-')
                            for i in histoico:
                                print(i)
                            print()

                    elif comprar == '2':
                        print('--LOJA DE ANIMAIS--')
                        print('----------------------------------------------------')
                        print('adicionar animais ao carrinho - 1')
                        print('comprar animais do carrinho - 2')
                        print('remover animais do carrinho - 3')
                        print('ver animais comprados - 4')
                        print('sair - 0')
                        print('----------------------------------------------------')
                        loja_animal = input('digite uma opçao: ')

    else:
        print('numero invalido, digite novamente')