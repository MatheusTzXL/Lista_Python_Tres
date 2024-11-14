def desenha_moldura(linhas=1, colunas=1):
    
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))


    print('+' + '-' * (colunas - 2) + '+')
    for _ in range(linhas - 2):
        print('|' + ' ' * (colunas - 2) + '|')
    if linhas > 1:
        print('+' + '-' * (colunas - 2) + '+')

desenha_moldura(10, 20)
