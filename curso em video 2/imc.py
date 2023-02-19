peso = float(input('digite seu peso em kg: '))
altura = float(input('digite sua altura em metros: '))
imc = peso / altura **2
print('seu imc é: {}'.format(imc))
if imc < 18.25:
    print('voce esta abaixo do peso')
elif 18.25 < imc < 25:
    print('voce esta no peso ideal')
elif 25 < imc < 30:
    print('voce esta acima do peso')
elif 30 < imc < 40:
    print('voce esta com obesidade')
else:
    print('voce esta com obesidade morbida')