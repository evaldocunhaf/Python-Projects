n = int(input('digite seu numero: '))
opção = int(input('''digite qual sera o tipo de conversão
[1]BINARIO
[2]HEXADECIMAL
[3]OCTAL \n'''))
if opção == 1:
    print('o seu numero ficou {}'.format(bin(n)))
elif opção == 2:
    print('o seu numero ficou {}'.format(hex(n)))
elif opção == 3:
    print('o seu numero ficou {}'.format(oct(n)))
else:
    print('erro')