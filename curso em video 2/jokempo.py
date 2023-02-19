import random
jm = random.randint(0, 2)
print('''bem vindo a jokempo
[0]pedra
[1]papel
[3]tesoura
''')
n = int(input('escolha a sua jogada'))
if n == 0 and jm == 1:
    print('voce perdeu!')
elif n == 1 and jm == 3:
    print('voce perdeu!')
elif n == 3 and jm == 0:
    print('voce perdeu!')
elif n == 1 and jm == 0:
    print('voce venceu')
elif n == 3 and jm == 1:
    print('voce venceu')
elif n == 0 and jm == 3:
    print('voce venceu')
else:
    print('deu empate')