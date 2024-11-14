def transforma_letra(texto):
    return texto.lower(), texto.upper()

texto = input("Digite um texto: ")
minusculo, maiusculo = transforma_letra(texto)
print(f"Minúsculas: {minusculo}")
print(f"Maiúsculas: {maiusculo}")
