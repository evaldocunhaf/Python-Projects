vogais = ''
tupla = ("evaldo", "agua", "nhoque", "linguado", "albacora")
for c in tupla:
    print(c)
    for n in c:
        if(n == "a" or n == "e" or n == "i" or n == "o" or n == "u"):
            vogais += n + " "
    print("as vogais da palavra {} são {}".format(c,vogais.split()))
    vogais = ''

