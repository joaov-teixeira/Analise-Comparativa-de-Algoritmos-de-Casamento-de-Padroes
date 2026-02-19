def computar_lps(padrao):
    """
    Cria a tabela de prefixos (Longest Prefix Suffix) para o KMP.
    Indica para onde pular no padrão em caso de falha.
    """
    m = len(padrao)
    lps = [0] * m
    comprimento = 0  # Comprimento do prefixo anterior mais longo
    i = 1

    while i < m:
        if padrao[i] == padrao[comprimento]:
            comprimento += 1
            lps[i] = comprimento
            i += 1
        else:
            if comprimento != 0:
                comprimento = lps[comprimento - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(texto, padrao):
    """
    Algoritmo Knuth-Morris-Pratt (KMP).
    [cite_start]Complexidade: O(n + m) [cite: 41]
    """
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    
    if m > n:
        return ocorrencias

    # Pré-processamento do padrão
    lps = computar_lps(padrao)
    
    i = 0  # Índice do texto
    j = 0  # Índice do padrão
    
    while i < n:
        if padrao[j] == texto[i]:
            i += 1
            j += 1

        if j == m:
            ocorrencias.append(i - j)
            j = lps[j - 1]
        elif i < n and padrao[j] != texto[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return ocorrencias