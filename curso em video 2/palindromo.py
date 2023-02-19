inverso = ''
frase = input('digite sua frase: ').upper()
fraseNoSpace = frase.replace(' ', '')
#aqui começa a reescrita da frase ao contrario usamos tudo com -1 para conseguir pegar todas as letras
#da frase e colocar elas ao contrario
for letra in range(len(fraseNoSpace) - 1, -1, -1):
    inverso += fraseNoSpace[letra]
if inverso == fraseNoSpace:
    print('a frase é um palindromo')
else:
    print('a frase não é um palindromo')