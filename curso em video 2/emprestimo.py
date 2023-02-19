print('calculador de emprestimo')
salario = float(input('digite seu salario: '))
casa = float(input('digite o valor da casa: '))
anos = int(input('digite a quantidade de anos que quer dividir: '))
prestação = casa / anos / 12
limite = salario * (30/100)
if prestação > limite:
    print('emprestimo negado')
else:
    print('emprestimo aceito com prestação mensal de R${}'.format(prestação))
