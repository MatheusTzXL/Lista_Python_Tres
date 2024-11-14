def primeiro_ultimo_nome(nome_completo):
    nomes = nome_completo.strip().split()
    return nomes[0], nomes[-1]

nome_completo = input("Digite seu nome completo: ")
primeiro, ultimo = primeiro_ultimo_nome(nome_completo)
print(f"Primeiro nome: {primeiro}")
print(f"Último nome: {ultimo}")
