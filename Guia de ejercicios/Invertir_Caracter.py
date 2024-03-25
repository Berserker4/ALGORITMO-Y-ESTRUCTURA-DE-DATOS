def invertir_Caracter(Caracter):
    if len(Caracter) <= 1:
        return Caracter
    else:
        return Caracter[-1] + invertir_Caracter(Caracter[:-1])
Caracter = "Buenas tardes"
print(invertir_Caracter(Caracter))
