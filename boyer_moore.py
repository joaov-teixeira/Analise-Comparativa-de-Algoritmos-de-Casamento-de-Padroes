def preprocessar_mau_caractere(padrao):
    """Cria a tabela de deslocamento para a heurística do Mau Caractere."""
    m = len(padrao)
    # Inicializa com -1 (não encontrado)
    tabela = [-1] * 256 
    for i in range(m):
        tabela[ord(padrao[i])] = i
    return tabela

def preprocessar_bom_sufixo(padrao):
    """Cria as tabelas para a heurística do Bom Sufixo."""
    m = len(padrao)
    bordas = [0] * (m + 1)
    shift = [0] * (m + 1)

    # Passo 1: Calcular bordas
    i = m
    j = m + 1
    bordas[i] = j
    while i > 0:
        while j <= m and padrao[i - 1] != padrao[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = bordas[j]
        i -= 1
        j -= 1
        bordas[i] = j

    # Passo 2: Preencher shifts restantes baseados no prefixo
    j = bordas[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bordas[j]
            
    return shift

def boyer_moore(texto, padrao):
    """
    Algoritmo Boyer-Moore completo (Mau Caractere + Bom Sufixo).
    """
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    
    if m > n:
        return ocorrencias

    # Pré-processamento
    bad_char = preprocessar_mau_caractere(padrao)
    good_suffix = preprocessar_bom_sufixo(padrao)
    
    s = 0  # Deslocamento do padrão em relação ao texto
    while s <= (n - m):
        j = m - 1
        
        # Varre da direita para a esquerda
        while j >= 0 and padrao[j] == texto[s + j]:
            j -= 1
            
        if j < 0:
            # Encontrou uma ocorrência
            ocorrencias.append(s)
            # Pula baseado no bom sufixo total (ou 1 se m=0)
            s += good_suffix[0]
        else:
            # Pula o máximo entre a regra do mau caractere e bom sufixo
            # bad_char[ord(texto[s+j])] pega a última ocorrencia do char do texto no padrão
            pulo_bc = j - bad_char[ord(texto[s + j])] if ord(texto[s + j]) < 256 else j + 1
            pulo_gs = good_suffix[j + 1]
            s += max(pulo_bc, pulo_gs)
            
    return ocorrencias