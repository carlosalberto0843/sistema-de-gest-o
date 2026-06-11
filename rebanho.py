def opcao1(animal, animal_lactacao, estoque_animal):
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
    return animal, animal_lactacao, estoque_animal

def opcao2(animal, animal_lactacao, estoque_animal,venda_animal):
    print('animais em lactaçao')
    print(animal_lactacao, '\n')
    print('animais para engorda')
    print(animal, '\n')
    print('animais em estoque')
    print(estoque_animal,'\n')
    print('animais postos á venda')  
    print(venda_animal ,'\n')

def opcao3(animal, animal_lactacao, estoque_animal):
    troca = input('qual o status do seu animal: ')
    if troca == 'lactacao':
        print(animal_lactacao)
        animal2 = input('digite o numero do animal: ')
        valor = input('digite o item que deseja alterar: ').lower()
        novo_valor = input('digie o novo valor: ')
        animal_lactacao[animal2][valor] = novo_valor
        if valor == 'status' and novo_valor == 'venda':
            animal_lactacao[animal2]['status'] = 'venda'
            estoque_animal[animal2] = animal_lactacao[animal2]
            animal_lactacao.pop(animal2)
        elif valor == 'status' and novo_valor == 'engorda':
            animal_lactacao[animal2]['status'] = 'engorda'
            animal[animal2] = animal_lactacao[animal2]
            animal_lactacao.pop(animal2)
    elif troca == 'engorda':
        print(animal)
        animal2 = input('digite o numero do animal: ')
        valor = input('digite o item que deseja alterar: ').lower()
        novo_valor = input('digie o novo valor: ')
        animal[animal2][valor] = novo_valor
        if valor == 'status' and novo_valor == 'venda':
            animal[animal2]['status'] = 'venda'
            estoque_animal[animal2] = animal[animal2]
            animal.pop(animal2)
        elif valor == 'status' and novo_valor == 'lactacao':
            animal[animal2]['status'] = 'lactacao'
            animal_lactacao[animal2] = animal[animal2]
            animal.pop(animal2)                           
    elif troca == 'venda':
        print(estoque_animal)
        animal2 = input('digite o numero do animal: ')
        valor = input('digite o item que deseja alterar: ').lower()
        novo_valor = input('digie o novo valor: ')
        estoque_animal[animal2][valor] = novo_valor
        if valor == 'status' and novo_valor == 'lactacao':
            estoque_animal[animal2]['status'] = 'lactacao'
            animal_lactacao[animal2] = estoque_animal[animal2]
            estoque_animal.pop(animal2)
    elif valor == 'status' and novo_valor == 'engorda':
        estoque_animal[animal2]['status'] = 'engorda'
        animal[animal2] = estoque_animal[animal2]
        estoque_animal.pop(animal2)
    else:
        print('algo deu errado tente novamente \n')
    
    return animal, animal_lactacao, estoque_animal

def opcao4(animal_lactacao):
    print(animal_lactacao)
    nu5 = input('digite o numero do animal: ')
    if nu5 in animal_lactacao:
        animal_lactacao.pop(nu5)   
        print('animal removido de lactaçao')
    else:
        print('animal nao removido')
    return animal_lactacao

def opcao5(animal):
    print(animal)
    nu5 = input('digite o numero do animal: ')
    if nu5 in animal:
        animal.pop(nu5)   
        print('animal removido de engorda')
    else:
        print('animal nao removido')
    return animal       

       

