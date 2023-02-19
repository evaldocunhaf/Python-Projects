n = input('qual operação voce deseja realizar?\n+ (soma)\n- (subtração)\nX (multiplicação)\n% (divisão)\n')
if n == '+':
    n = float(input('digite o primeiro numero: '))
    n0 = float(input('digite o numero a ser somado: '))
    resultado = n + n0
    print('resultado = {}'.format(resultado))
    while True:
        n1 = (input('digite o numero a ser somado ou sair: '))
        if n1 == 'sair':
            break
        else:
            n1 = float(n1)
            resultado = resultado + n1
            print('resultado = {}'.format(resultado))
if n == '-':
    n = float(input('digite o primeiro numero: '))
    n0 = float(input('digite o numero para subtraido: '))
    resultado = n - n0
    print('resultado = {}'.format(resultado))
    while True:
        n1 = (input('digite o numero para subtrair ou sair: '))
        if n1 == 'sair':
            break
        else:
            n1 = float(n1)
            resultado = resultado - n1
            print('resultado = {}'.format(resultado))
if n == 'x':
    n = float(input('digite o primeiro numero: '))
    n0 = float(input('digite o numero a ser multiplicado: '))
    resultado = n * n0
    print('resultado = {}'.format(resultado))
    while True:
        n1 = (input('digite o numero a ser multiplicado ou sair: '))
        if n1 == 'sair':
            break
        else:
            n1 = float(n1)
            resultado = resultado * n1
            print('resultado = {}'.format(resultado))
if n == '%':
    n = float(input('digite o primeiro numero: '))
    n0 = float(input('digite o numero a dividir: '))
    resultado = n / n0
    print('resultado = {}'.format(resultado))
    while True:
        n1 = (input('digite o numero a dividir ou sair: '))
        if n1 == 'sair':
            break
        else:
            n1 = float(n1)
            resultado = resultado / n1
            print('resultado = {}'.format(resultado))