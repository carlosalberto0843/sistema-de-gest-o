adm = []
clientes = []
animal = []
produzido_lactaçao = []
estoque_animal = []
estoque_produtos = []
venda_animal = []
venda_produtos = []
op = -99
while op != 0:
    print('----BEM VINDO AO SISTEMA DE GESTAO AGROPECUARIA----')
    print('cadastrar cliente - 1:')
    print('cadastrar adm - 2:')
    print('login - 3')
    op = int(input('digite numero: '))

    if op == 1:
        nome = input('digite seu nome: ')
        senha = input('digite sua senha: ')
        clientes.append([nome , senha])
        print('conta criada em cliente')

    elif op == 2:
        nome2 = input('digite seu nome: ')
        senha2 = input('digite sua senha: ')
        adm.append([nome2 , senha2])
        print('conta criada em adm')
    
    
    elif op == 3: #LOGIN #nao esquecer do else no final
        login = input('diga a login: ')
        senha = input('diga a senha: ')
        bv = False
        for a in clientes:
                if login == a[0] and senha == a[1]:
                    print(f'bem vindo {login}')         
        for a in adm:
                if login == a[0] and senha == a[1]:
                    print(f'seja bem vindo {login}') #nao esquecer do else no final
                    while True:
                        bv = True                                      
                        print('---escolha uma opçao---')
                        print('Gerenciar Rebanho - [1]')
                        print('gerenciar producao e derivados - [2]')
                        print('logout - [0]')
                        geral = input('escolha a opçao: ')
                        if geral == '0':
                            print('--------')                        
                            print('ate mais')
                            print('--------')
                            break
                        elif geral == '1':
                            print('---gerenciar rebanho---')
                            print('Cadastrar animal - [1]')
                            print('buscar - [2]')
                            print('atualizar - [3]')
                            print('remover animais em lactaçao - [4]')
                            gr = input('escolha a sua opçao: ')
                            if gr == '1':
                                l1 = input('qual o tipo de animal - [Bovino de Leite, Caprino, Ovino, Suíno/Leitão]: ')
                                l2 = int(input('qual a identificaçao do animal? - [brinco/número]: '))
                                l3 = input('qual o status do animal? - [lactaçao, engorda, venda]: ')
                                if l3 == 'lactaçao' or l3 == 'engorda':
                                    animal.append([l1, l2, l3, []])
                                    print('animal adcionado')
                                    continue
                                elif l3 == 'venda':
                                    estoque_animal.append([l1, l2, l3, []])
                                    print('animal adcionado')
                                    continue

                            elif gr == '2':
                                buscar = int(input('digite o numero do animal: '))
                                for item in animal:
                                    if item[1] == buscar:  # só o ID
                                        print(f'o animal é: {item}')    

                            elif gr == '3': 
                                print(f'animais em {animal}')
                                print(f'animais em {estoque_animal}')
                                mudar = input('o animal desejado é de lactaçao, engorda ou venda: ')
                                atualizar = input('deseja mudar para lactaçao, engorda ou venda: ')
                                num = int(input('digite o numero do animal: '))
                                trocar = False
                                if (mudar == 'lactaçao'or mudar == 'engorda') and atualizar == 'venda':
                                    for troca in animal:
                                        if troca[1] == num:
                                            troca[2] = 'venda'
                                            estoque_animal.append(troca)
                                            animal.remove(troca)
                                            print('animal atualizado')
                                            trocar = True
                                            break
                                elif  mudar == 'venda' and atualizar == 'lactaçao':
                                    for troca in estoque_animal:
                                        if troca[1] == num:
                                            troca[2] = 'lactaçao'
                                            animal.append(troca)
                                            estoque_animal.remove(troca)
                                            print('animal atualizado')
                                            trocar = True
                                            break
                                elif mudar == 'venda' and atualizar == 'engorda':
                                    for troca in estoque_animal:
                                        if troca[1] == num:
                                            troca[2] = 'engorda'
                                            animal.append(troca)
                                            estoque_animal.remove(troca)
                                            print('animal atualizado')
                                            trocar = True
                                            break
                                if not trocar:
                                        print('nao atualizado, digite novamente')

                            if gr == '4':
                                print(animal)
                                nu5 = int(input('digite o numero do animal: '))
                                achei = False
                                for im in animal:
                                    if im[1] == nu5:
                                        animal.remove(im)
                                        print('animal removido de lactaçao')
                                        achei = True
                                          
                        elif geral == '2':
                            print('----gerenciar producao e derivados----')
                            print('gerenciar produçao diaria - [1]')
                            print('gerenciar estoque de animal  - [2]')
                            print('gerenciar estoque de produtos - [3]')
                            print('gerenciar itens para a venda - [4]')
                            print('voltar - [0]')
                            escolha = int(input('selecione uma opcao: '))
                            if escolha == 1:
                                print('----GERENCIAR PRODUÇAO DIARIA----')
                                print('cadastar produçao diaria - [1]')
                                print('ver produçao diaria de um animal - [2]')
                                print('remover item - [3]')
                                print('por para a venda - [4]')
                                diaria = int(input('escolha uma opçao: '))
                                if diaria == 1:
                                    colocar = int(input('digite o numero do animal em lactaçao:'))
                                    ad = -1
                                    for i in range(len(animal)):
                                        if animal[i][1] == colocar:
                                            print(animal[i])
                                            ad = int(input('quantos litros de leite foi produzido por esse animal: '))
                                            ad1 = input('data de expediçao do leite: ')
                                            produzido_lactaçao.append([colocar, ad ,ad1])
                                            ad = 0

                                    if ad == 0:
                                        print('produto adicionado')

                                    else:
                                        print('produto nao adicionado')
                                elif diaria == 2:
                                    colocar2 = int(input('digite o numero do animal: '))
                                    for i in range(len(produzido_lactaçao)):
                                        if produzido_lactaçao[i][0] == colocar2:
                                            print(produzido_lactaçao[i])
                                            print('')

                            elif escolha == 2:
                                print('----gerenciar estoque de animal----') #gerenciar estoque de animal
                                print('ver animais em estoque - [1]')
                                print('remover animais do estoque - [2]')
                                print('inserir animal a venda -[3]')
                                print('voltar - [0]')
                                escolha_animal = int(input('digite a opcao desejada: '))
                                if escolha_animal == 1:
                                    for itens in estoque_animal:
                                        print(itens)
                                    print('')

                                elif escolha_animal == 3:
                                    print(escolha_animal)
                                    nu = int(input('digite numero do animal: '))
                                    dinheiro = float(input('digite o valor do animal para venda: '))
                                    achei = -1
                                    for ites in range(len(estoque_animal)):
                                        if estoque_animal[ites][1] == nu:
                                            estoque_animal[ites][3] = dinheiro
                                            index = ites

                                    if index >= 0:
                                        venda_animal.append(estoque_animal[index])
                                        estoque_animal.pop(index)
                                        print('animal adicionado a venda')

                                    else:
                                        print('animal nao adicionado, digite o numero novamente')

                            elif escolha == 3:
                                print('----gerenciar estoque de produtos----') #gerenciar estoque de produtos
                                print('ver protutos no estoque atual - [1]')
                                print('adicionar protudos ao estoque - [2]')
                                print('remover produtos do estoque - [3]')
                                print('colocar protutos a venda - [4]')
                                print('voltar - [5]')
                                escolha_protudos = int(input('digite a opcao desejada: '))
                                if escolha_protudos == 1:
                                    for itens in estoque_produtos:
                                        print(itens)
                                    print('')

                                elif escolha_protudos == 2:
                                    pro1 = input('digite o nome do produto: ')
                                    pro2 = float(input('digite a quantidade desse produto em kg ou litros: '))
                                    pro3 = input('digite a data de hoje: ')
                                    pro4 = int(input('digite numero para a indentificaçao: '))
                                    estoque_produtos.append([pro4, pro1, pro2 ,pro3, []])
                                
                                elif escolha_protudos == 3:
                                    print(estoque_produtos)
                                    remo = int(input('digite o numero do produto: '))
                                    remove =  False
                                    for remover in estoque_produtos:
                                        if remover[0] == remo:
                                            estoque_produtos.pop(remover)
                                            print('protudo removido com sucesso')
                                            remove = True
                                            break
                                    if not remove:
                                        print('produto nao removido, digite novamente')

                                elif escolha_protudos == 4:
                                    colocar_venda = int(input('digite o numero do produto: '))
                                    index = -1
                                    for i in range(len(estoque_produtos)):
                                        if estoque_produtos[i][0] == colocar_venda:
                                            index = i
                                            break
                                    
                                    if index >= 0:
                                        preco = float(input('digite o valor do produto: '))
                                        venda_produtos.append(estoque_produtos[index])
                                        venda_produtos[index][4].append(preco)
                                        estoque_produtos.pop(index)
                                        print('produto inserido para venda')
                                    else:
                                        print('produto nao inserido')

                            elif escolha == 4:
                                print('----LISTA DE VENDAS----')
                                print('vendas de animais - [1] ')
                                print('vendas de produtos - [2]')
                                vender = int(input('digite a opcao: '))
                                if vender == 1:
                                    print('----VENDA ANIMAL----')   
                                    print('ver itens a venda - [1]')
                                    print('remover itens da venda - [1]')
                                    print('mudar preço de itens da venda - [3]')
                                    animais_venda = int(input('digite a opcao desejada: '))
                                    if animais_venda == 1:
                                        for i in venda_animal:
                                            print(i)
                                        print('')

                                elif vender == 2:
                                    print('----VENDA PRODUTOS----')   
                                    print('ver itens a venda - [1]')
                                    print('remover itens da venda - [2]')
                                    print('mudar preço de itens da venda - [3]')
                                    produto_venda = int(input('digite a opcao desejada: '))
                                    if produto_venda == 1:
                                        for f in venda_produtos:
                                            print(f)
                                        print('') 
                                    
                                    elif animais_venda == 2:
                                        for i in animais_venda:
                                            print(i)
                                        print('')
                                        produto_venda = int(input('digite o numero do produto: '))
                                        index = -1
                                        for i in range(len(venda_produtos)):
                                            if venda_produtos[i][0] == venda_produtos:
                                                index = i
                                                break
                                        if index >= 0:
                                            venda_produtos.pop(index)
                                            print('produto removido')
                                        else:
                                            print('produto nao removido')
                                    
                                    elif produto_venda == 3:
                                        troca_venda = int(input('digite o numero do animal: '))
                                        index = -1
                                        for i in range(len(venda_produtos)):
                                            if venda_produtos[i][0] == troca_venda:
                                                index = i
                                                break

                                        if index >= 0:
                                            novo_preco = float(input('digite o novo preço: '))
                                            venda_produtos[index].pop(venda_produtos[4])
                                            venda_produtos[index][4].append(novo_preco)
                                            print('novo preço atualizado')
                                        
                                        else:
                                            print('algo deu errado')