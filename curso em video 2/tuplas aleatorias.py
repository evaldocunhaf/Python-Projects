import random as r
n = (r.randint(1, 10), r.randint(1, 10), r.randint(1, 10), r.randint(1, 10), r.randint(1, 10))
nmaior = n[0]
nmenor = n[0]
for c in n:
    parametro = c
    if parametro < nmenor:
        nmenor = parametro
    elif parametro > nmaior:
        nmaior = parametro
print(n)
print('o maior numero é {}'.format(nmaior))
print('o menor numero é {}'.format(nmenor))