import math
dnascimento = int(input('digite seu dia de nascimento: '))
mnascimento = int(input('digite seu mês de nascimento: '))
anascimento = int(input('digite seu ano de nascimento: '))
if anascimento < 2005:
    print('voce esta atrasdo para o alistamento')
    print('seu atraso é de {} anos'.format(math.sqrt((anascimento - 2005)**2)))
elif anascimento > 2005:
    print('voce nao pode se alistar agora')
    print('você precisa esperar {} anos'.format(math.sqrt((anascimento - 2005)**2)))
else:
    print('você precisa se alistar esse ano!')