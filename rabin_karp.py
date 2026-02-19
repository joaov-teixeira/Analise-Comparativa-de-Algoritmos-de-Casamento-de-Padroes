# rabin_karp.py

def rabin_karp(texto, padrao):
    """
    Algoritmo Rabin-Karp usando Rolling Hash.
    [cite_start]Complexidade Média: O(n + m) [cite: 35]
    """
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    
    if m > n:
        return ocorrencias
    
    # Configurações do Hash
    d = 256  # Tamanho do alfabeto (ASCII)
    q = 101  # Número primo para módulo
    
    p = 0    # Hash do padrão
    t = 0    # Hash da janela do texto
    h = 1    # Multiplicador para o dígito mais significativo
    
    # Calcula h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Calcula hash inicial do padrão e da primeira janela do texto
    for i in range(m):
        p = (d * p + ord(padrao[i])) % q
        t = (d * t + ord(texto[i])) % q

    # Desliza o padrão sobre o texto
    for i in range(n - m + 1):
        # Se os hashes coincidem, verifica caracteres (para evitar colisão)
        if p == t:
            match = True
            for j in range(m):
                if texto[i + j] != padrao[j]:
                    match = False
                    break
            if match:
                ocorrencias.append(i)

        # Calcula hash da próxima janela (Rolling Hash)
        if i < n - m:
            t = (d * (t - ord(texto[i]) * h) + ord(texto[i + m])) % q
            # Garante que t seja positivo
            if t < 0:
                t = t + q
                
    return ocorrencias