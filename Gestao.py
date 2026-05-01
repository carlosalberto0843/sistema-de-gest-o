adm = []
lista_g = []
identificaçao =[]
status = []
rebanho = []
clientes = []
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
    
    
    elif op == 3: #LOGIN ADM
        login = input('diga a login: ')
        senha = input('diga a senha: ')
        bv = False
        for a in clientes:
                if login == a[0] and senha == a[1]:
                    print(f'bem vindo {clientes[0][0]}')         
        for a in adm:
                if login == a[0] and senha == a[1]:
                    print(f'seja bem vindo {adm[0][0]}')
                    while True:
                        bv = True    
                        print('---escolha uma opçao---')
                        print('Gerenciar Rebanho - [1]')
                        print('gerenciar producao e derivados - [2]')
                        print('logoof - [0]')
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
                            print('atualizar - [2]')
                            print('remover animais - [3]')
                            gr = input('escolha a sua opçao: ')
                            if gr == '1':
                                rebanho.append(input('qual o tipo de animal - [Bovino de Leite, Caprino, Ovino, Suíno/Leitão] '))
                                identificaçao.append(input('qual a identificaçao do animal? - [brinco/número]'))
                                status.append(input('qual o status do animal? - [em lactação, para engorda, disponível para venda]'))
                                lista_g.append([rebanho,identificaçao,status])
                                print(lista_g)
                                print('animal adcionado')
                                continue
                            elif geral == '2':
                                buscar = input('oque deseja buscar: ')