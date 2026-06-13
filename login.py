def login_clientes(clientes):    
    nome = input('digite seu nome: ')
    senha = input('digite sua senha: ')
    if nome in clientes:
        print('nome do usuario ja existente, digite outro nome \n')
    else:    
        clientes[nome] = senha
        print('conta criada em cliente')
    return clientes

def login_adm(adm): 
    nome2 = input('digite seu nome: ')
    senha2 = input('digite sua senha: ')
    if nome2 in adm:
            print('nome do usuario ja existente, digite outro nome \n')
    else:
        adm[nome2] = senha2
        print('conta criada em adm')
    return adm