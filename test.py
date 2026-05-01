animal = [['vaca', 2020 , 'ativa',]]
buscar = int(input('qual o numero do animal?: '))

for item in animal:
    if item[1] == buscar:
        print(item)

