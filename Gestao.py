adm = []
clientes = []
animal = []
estoque_animal = []
estoque_produtos = []
venda_animal = []
venda_produtos = []
a1 = ''
a2 = ''
a3 = ''
op = -99
while op != 0:
    print('----MENU----')
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
                            print('remover animais - [4]')
                            gr = input('escolha a sua opçao: ')
                            if gr == '1':
                                l1 = input('qual o tipo de animal - [Bovino de Leite, Caprino, Ovino, Suíno/Leitão]: ')
                                l2 = int(input('qual a identificaçao do animal? - [brinco/número]: '))
                                l3 = input('qual o status do animal? - [lactação, engorda, venda]: ')
                                if l3 == 'lactação' or l3 == 'engorda':
                                    animal.append([l1, l2, l3])
                                    print('animal adcionado')
                                    continue
                                elif l3 == 'venda':
                                    estoque_animal.append([l1, l2, l3])
                                    print('animal adcionado')
                                    continue

                            elif gr == '2':
                                buscar = int(input('digite o numero do animal: '))
                                for item in animal:
                                    if item[1] == buscar:  # só o ID
                                        print(f'o animal é: {item}')                     
                        
                        elif geral == '2':
                            print('----gerenciar producao e derivados----')
                            print('cadastar produçao diaria - [1]')
                            print('gerenciar estoque de animal  - [2]')
                            print('gerenciar estoque de produtos - [3]')
                            print('gerenciar itens para a venda - [4]')
                            print('voltar - [0]')
                            escolha = int(input('selecione uma opcao: '))
                            if escolha == 1:
                                print('----gerenciar estoque de animal----') #gerenciar estoque de animal
                                print('ver animais em estoque - [1]')
                                print('remover animais do estoque - [3]')
                                print('inserir animal a venda -[4]')
                                print('voltar - [0]')
                                escolha_animal = int(input('digite a opcao desejada: '))
                                if escolha_animal == 2:
                                    for itens in estoque_animal:
                                        print(itens)
                                elif escolha_animal == 4:
                                    nu = int(input('digite numero do animal: '))
                                    achei = False
                                    for itens in estoque_animal:
                                        if item[1] == nu:
                                            venda_animal.append(itens)
                                            estoque_animal.remove(itens)
                                            print('animal adicionado com sucesso')
                                            achei = True
                                            break
                                    if not achei:
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
                                    for itens in escolha_protudos:
                                        print(itens)
                                    print('')
                                elif escolha_protudos == 2:
                                    pro1 = input('digite o nome do produto: ')
                                    pro2 = float(input('digite a quantidade desse produto em kg ou litros: '))
                                    pro3 = input('digite a data de hoje: ')
                                    pro4 = int(input('digite numero para a indentificaçao: '))
                                    estoque_produtos.append([pro1, pro2 ,pro3])