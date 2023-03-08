n = []
while True:
    valor =input('digite um valor para ser adicionado na lista ou digite pare: ')
    if valor == 'pare':
        break
    else:
        valor = int(valor)
        if valor not in n:
            n.append(valor)
            print(n)
        else:
            print('esse numero ja tem na lista')
n.sort()
print('a lista ficou: {}'.format(n))