import time
import random
import string
import matplotlib.pyplot as plt
try:
    from brute_force import forca_bruta
    from rabin_karp import rabin_karp
    from knuth_morris_prattKMP import kmp
    from boyer_moore import boyer_moore
    from boyer_moore_horspool import bm_horspool
    from boyer_moore_horspool_sunday import bm_sunday
except ImportError as e:
    print(f"Erro na importação: {e}")
    print("Dica: Verifique se renomeou 'knuth_morris_pratt(KMP).py' para 'knuth_morris_pratt.py'")
    exit()

# Lista de algoritmos para iterar
ALGORITMOS = [
    ("Força Bruta", forca_bruta),
    ("Rabin-Karp", rabin_karp),
    ("KMP", kmp),
    ("Boyer-Moore", boyer_moore),
    ("Horspool", bm_horspool),
    ("Sunday", bm_sunday)
]

# --- FUNÇÕES AUXILIARES ---

def gerar_texto(tamanho, alfabeto=string.ascii_letters + string.digits + " "):
    """Gera uma string aleatória de tamanho N com o alfabeto dado."""
    return ''.join(random.choices(alfabeto, k=tamanho))

def medir_tempo(algoritmo_func, texto, padrao):
    """Executa o algoritmo e retorna o tempo gasto em segundos."""
    inicio = time.time()
    algoritmo_func(texto, padrao)
    fim = time.time()
    return fim - inicio

# --- CENÁRIOS DE TESTE ---

def executar_testes():
    print(f"{'CENÁRIO':<40} | {'ALGORITMO':<15} | {'TEMPO (s)':<10} | {'OCORRÊNCIAS'}")
    print("-" * 90)

    # Definição dos parâmetros de teste
    # Tamanhos de Texto: Pequeno (1k), Médio (100k), Grande (1M)
    # Alfabetos: DNA (4 letras) vs ASCII (256 letras)
    
    cenarios = [
        # Cenário 1: Texto Pequeno, Padrão Curto, Alfabeto Grande (Texto comum)
        {"nome": "Texto 10k | Padrão 5 chars | ASCII", 
         "tam_texto": 10_000, "tam_padrao": 5, "alfabeto": string.printable},
         
        # Cenário 2: Texto Médio, Padrão Médio, Alfabeto Grande
        {"nome": "Texto 100k | Padrão 50 chars | ASCII", 
         "tam_texto": 100_000, "tam_padrao": 50, "alfabeto": string.printable},

        # Cenário 3: Texto Grande, Padrão Longo, DNA (Muitas repetições)
        # DNA é o "pior caso" para muitos algoritmos pois tem pouca variedade de letras
        {"nome": "Texto 500k | Padrão 100 chars | DNA", 
         "tam_texto": 500_000, "tam_padrao": 100, "alfabeto": "ACGT"},
    ]

    resultados_grafico = {alg[0]: [] for alg in ALGORITMOS}
    labels_cenarios = []

    for config in cenarios:
        # 1. Preparação dos dados
        texto = gerar_texto(config["tam_texto"], config["alfabeto"])
        
        # Garante que o padrão existe pelo menos uma vez no final para evitar "melhor caso" falso
        padrao = gerar_texto(config["tam_padrao"], config["alfabeto"])
        texto += padrao 
        
        labels_cenarios.append(config["nome"].split('|')[0].strip()) # Nome curto para o gráfico

        print(f"--- Rodando: {config['nome']} ---")

        for nome_alg, funcao in ALGORITMOS:
            try:
                # Rodamos 3 vezes e pegamos a média para estabilidade
                tempos = []
                for _ in range(3):
                    t = medir_tempo(funcao, texto, padrao)
                    tempos.append(t)
                
                tempo_medio = sum(tempos) / len(tempos)
                
                # Executa uma vez extra só para contar ocorrências (validar corretude)
                ocorrencias = len(funcao(texto, padrao))
                
                print(f"{config['nome']:<40} | {nome_alg:<15} | {tempo_medio:.6f} s | {ocorrencias}")
                
                # Guarda para o gráfico
                resultados_grafico[nome_alg].append(tempo_medio)

            except Exception as e:
                print(f"Erro no {nome_alg}: {e}")

        print("-" * 90)

    return labels_cenarios, resultados_grafico

# --- PLOTAGEM DE GRÁFICOS ---

def plotar_resultados(labels, dados):
    x = range(len(labels))
    largura = 0.1
    fig, ax = plt.subplots(figsize=(10, 6))

    for i, (nome_alg, tempos) in enumerate(dados.items()):
        posicao = [p + i * largura for p in x]
        ax.bar(posicao, tempos, largura, label=nome_alg)

    ax.set_xlabel('Cenários')
    ax.set_ylabel('Tempo (segundos)')
    ax.set_title('Comparação de Desempenho: Algoritmos de Busca')
    ax.set_xticks([p + 2.5 * largura for p in x])
    ax.set_xticklabels(labels)
    ax.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Iniciando bateria de testes...\n")
    labels, dados = executar_testes()
    plotar_resultados(labels, dados)