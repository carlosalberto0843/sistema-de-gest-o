adm = []
clientes = []
animal = []
estoque = []
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
                                l3 = input('qual o status do animal? - [em lactação, para engorda, disponível para venda]: ')
                                animal.append([l1, l2, l3])
                                print('animal adcionado')
                                continue
                            elif gr == '2':
                                buscar = int(input('digite o numero do animal: '))
                                for item in animal:
                                    if item[1] == buscar:  # só o ID
                                        print(f'o animal é: {item}')                     
                        elif geral == '2':
                            while True:
                                print('----gerenciar producao e derivados----')
                                print('cadastre de produçao diaria - [1]')
                                print('gerenciar estoque - [2]')
                                print('voltar - [3]')
                                escolha = int(input('selecione uma opcao: '))
                                if escolha == 1:
                                    nu = int(input('digite o numero do animal: '))
                                    for loop in animal:
                                        if loop[1] == nu:
                                            print(loop)
                                            diaria = input('qual produto foi produzido: ')
                                            diaria2 = float(input('quanto produzido: '))
                                            diaria3 = float(input('qual o valor para venda: '))                                 
                                            estoque.append([ nu, diaria, diaria2, diaria3])
                                            print(estoque)
                                
                                elif escolha == 2:
                                    print(f'----bem vindo {login} oque deseja fazer---- ')
                                    print('ver protutos no estoque atual - [1]')
                                    print('ver produdos especificos no estoque - [2]')
                                    print('colocar um animal para a venda - [3]')
                                    print('remover produtos do estoque - [4]')
                                    print('voltar - [5]')
                                    escolha_estoque = int(input('digite a opcao desejada: '))
                                    if escolha_estoque == 1:
                                            for itens in estoque:
                                                print(itens)
                                            print('')

                                    elif escolha == 3:
                                        nu = int(input('digite o numero do animal: '))
                                        for loop in animal:
                                            if loop[1] == nu:
                                                v1 = input('tipo de animal: ')
                                                v2 = float(input('peso do animal:'))
                                                v3 = float(input('valor do animal: '))
                                                estoque.append([nu, v1 ,v2 ,v3])

                                elif escolha == 3:
                                    break