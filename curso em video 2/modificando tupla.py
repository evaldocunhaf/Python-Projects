n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))
n4 = float(input('digite o quarto numero: '))
n = (n1, n2, n3, n4)
print('o numero 9 apareceu {} vezes'.format(n.count(9)))
print('o numero 3 aparece no termo {}'.format(n.index(3)))
for c in n:
    if (c % 2) == 0:
        print('teve o numero {} par'.format(c))