l0 = float(input('digite o valor do primeiro lado: '))
l1 = float(input('digite o valor do segundo lado: '))
l2 = float(input('digite o valor do ultimo lado: '))
if l0 < l1 + l2 or l1 < l0 + l2 or l2 < l0 + l1:
    print('o traingulo pode ser feito')
    if l1 == l2 or l2 == l0 or l0 == l1:
        print('o triangulo é isosceles')
    elif l1 == l2 == l0:
        print('o triangulo é equilatero')
    else:
        print('o triangulo é escaleno')
else:
    print('não pode formar um triangulo')