maiornumero = 0
menornumero = 0
n = []
for c in range (0,5):
    n.append(int(input('insira um valor na lista')))
    if n[c] >= maiornumero:
        maiornumero = n[c]
    elif n[c] <= menornumero:
        menornumero = n[c]
print('a lista ficou {}'.format(n))
print('o maior numero foi {} '.format(maiornumero), end="")
for i, v in enumerate(n):
    if v == maiornumero:
        print('na posição {}...'.format(i), end='')
print('o menor numero foi {} '.format(menornumero), end="")
for i, v in enumerate(n):
    if v == menornumero:
        print('na posição {}...'.format(i), end='')

