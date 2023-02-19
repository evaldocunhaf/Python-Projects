print('======tirador de médias=======')
n0 = float(input('digite o primeiro numero: '))
n1 = float(input('digite o segundo numero: '))
total = n0 + n1
divisor = 2
while True:
    continuidade = input('digite o proximo numero ou resultado para calcular a média: ')
    if continuidade == 'resultado':
        break
    else:
        continuidade = float(continuidade)
        total = total + continuidade
        divisor = divisor + 1
print('o resultado foi {}'.format(total / divisor))
