n = []
contagem5 = 0
while True:
    valor = input('digite um valor a ser registrado na lista ou pare para encerrar: ')
    if valor == 'pare':
        break
    else:
        valor = int(valor)
        n.append(valor)
        if valor == 5:
            contagem5 += 1
print('a lista final ficou {}'.format(n))
n.sort(reverse=True)
print('a lista em ordem decrescente ficou {}'.format(n))
print('a lista teve {} elementos'.format(len(n)))
if contagem5 >= 1:
    print('a lista teve o numero 5 e foi digitado {} vezes'.format(contagem5))