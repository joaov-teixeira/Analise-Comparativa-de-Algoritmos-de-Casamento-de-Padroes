def preprocessar_horspool(padrao):
    """
    Tabela de deslocamentos para Horspool.
    Shift = m - 1 - indice_da_ultima_ocorrencia (exceto o último char)
    """
    m = len(padrao)
    tabela = {}
    
    # Valor padrão de salto é o tamanho do padrão
    # Usamos dicionário para suportar qualquer caractere Unicode se necessário
    # Mas para lógica simples, assumimos chars presentes no texto
    
    for i in range(m - 1):
        tabela[padrao[i]] = m - 1 - i
        
    return tabela

def bm_horspool(texto, padrao):
    """
    Algoritmo Boyer-Moore-Horspool.
    Usa apenas a heurística do Mau Caractere simplificada.
    """
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    
    if m > n:
        return ocorrencias

    # Pré-processamento
    tabela = preprocessar_horspool(padrao)
    
    i = m - 1 # Índice no texto (alinhado com o fim do padrão)
    
    while i < n:
        k = 0
        # Comparação da direita para a esquerda
        while k < m and padrao[m - 1 - k] == texto[i - k]:
            k += 1
            
        if k == m:
            ocorrencias.append(i - m + 1)
        
        # Cálculo do salto
        # Olha para o caractere do texto onde a janela termina (texto[i])
        # Se o caractere existe na tabela, usa o valor, senão pula m
        salto = tabela.get(texto[i], m)
        i += salto
        
    return ocorrencias