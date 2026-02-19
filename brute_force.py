def forca_bruta(texto, padrao):
    """
    Algoritmo de Força Bruta para casamento de padrões.
    Verifica todas as posições possíveis do texto.
    
    [cite_start]Complexidade Pior Caso: O(n * m) [cite: 29]
    """
    n = len(texto)
    m = len(padrao)
    ocorrencias = []

    # Se o padrão for maior que o texto, não há ocorrência
    if m > n:
        return ocorrencias

    # Percorre o texto até onde o padrão ainda cabe
    for i in range(n - m + 1):
        j = 0
        # Compara caractere a caractere
        while j < m and texto[i + j] == padrao[j]:
            j += 1
        
        # Se percorreu todo o padrão, encontrou
        if j == m:
            ocorrencias.append(i)
            
    return ocorrencias