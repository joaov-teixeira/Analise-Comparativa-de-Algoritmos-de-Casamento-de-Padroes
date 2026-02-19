# Análise Comparativa de Algoritmos de Casamento de Padroes:
<img width="1000" height="600" alt="grafico_resultados" src="https://github.com/user-attachments/assets/d0fbeffb-9bc4-4ad6-bcb3-1a90d77ee436" />
Abusca de padrões em strings é um problema clássico da Ciência da Computação, com
aplicações diretas em editores de texto, ferramentas de busca, bioinformática, detecção
de plágio e sistemas de recuperação da informação. O problema consiste, formalmente,
em encontrar todas as ocorrências de um padrão P de tamanho m dentro de um texto T
de tamanho n.
Este trabalho prático tem como objetivo implementar, comparar e analisar o compor
tamento de diferentes algoritmos de busca de padrões, focando tanto na complexidade
teórica quanto no desempenho empírico em diferentes cenários.

# Os algoritmos analisados são:
Força Bruta
Rabin-Karp
Knuth-Morris-Pratt (KMP)
Boyer-Moore
Boyer-Moore-Horspool
Boyer-Moore-Horspool-Sunday

# Metodologia:
## Implementação e Ambiente:
Os algoritmos foram implementados na linguagem Python. Os testes foram realizados
em umambiente computacional pessoal, medindo-se o tempo de CPU (em segundos) para
a execução completa da busca.
## Cenários de Teste:
Foram definidos três cenários distintos para avaliar o comportamento dos algoritmos
sob diferentes condições de tamanho de entrada e alfabeto:
## Cenário 1 (Texto Pequeno): Texto de 10.000 caracteres, padrão de 5 caracteres, alfabeto ASCII completo.
## Cenário 2 (Texto Médio): Texto de 100.000 caracteres, padrão de 50 caracteres, alfabeto ASCII completo.
## Cenário 3 (DNA / Pior Caso para Heurísticas): Texto de 500.000 caracteres, padrão de 100 caracteres, alfabeto reduzido (A, C, G, T). Este cenário simula bioinformática e testa a eficiência dos saltos em alfabetos pequenos.

# Conclusão
[relatorio_AEDS2_joaoTeixeira.pdf](https://github.com/user-attachments/files/25425946/relatorio_AEDS2_joaoTeixeira.pdf)
## Melhor Desempenho Geral: 
A família Boyer-Moore é imbatível na prática. O algoritmo Horspool oferece o melhor equilíbrio, sendo muito rápido e extremamente simples de implementar.
## Simplicidade vs. Eficiência:
Para textos aleatórios comuns, a Força Bruta ainda é uma opção viável e até mais rápida que algoritmos complexos como o KMP, devido à simplicidade de suas instruções de máquina.
## Compensação do Pré-processamento: 
O custo de pré-processamento do Boyer Moore compensa amplamente, pois permite pular grandes seções do texto. Já o pré processamento do KMP não se justificou nestes testes práticos com dados aleatórios.
## Recomendação:
Para implementações gerais em linguagens de alto nível, recomenda se o uso do Boyer-Moore-Horspool devido à sua facilidade de manutenção e alta performance, exceto em casos muito específicos de alfabetos minúsculos onde o Boyer-Moore completo pode ter vantagem.
