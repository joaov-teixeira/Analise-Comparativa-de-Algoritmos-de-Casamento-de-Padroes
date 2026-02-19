def preprocessar_sunday(padrao):
    """
    Tabela de deslocamentos para Sunday.
    Shift = m - indice_da_ultima_ocorrencia
    """
    m = len(padrao)
    tabela = {}
    
    for i in range(m):
        tabela[padrao[i]] = m - i
        
    return tabela

def bm_sunday(texto, padrao):
    """
    Algoritmo Boyer-Moore-Horspool-Sunday.
    Olha o caractere logo APÓS a janela atual para definir o salto.
    """
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    
    if m > n:
        return ocorrencias

    # Pré-processamento
    tabela = preprocessar_sunday(padrao)
    
    i = 0
    while i <= n - m:
        j = 0
        # Verifica casamento
        while j < m and texto[i + j] == padrao[j]:
            j += 1
            
        if j == m:
            ocorrencias.append(i)
            
        # Pulo
        if i + m < n:
            # Olha o caractere APÓS o padrão (texto[i+m])
            # Se não existir no padrão, pula m + 1
            # Se existir, alinha esse caractere com o do padrão
            salto = tabela.get(texto[i + m], m + 1)
            i += salto
        else:
            break
            
    return ocorrencias