# PageRank: MPI (mpi4py) vs Spark (PySpark)

Trabalho 2 de Sistemas Distribuídos (UFF). Comparação de desempenho entre
duas implementações paralelas do PageRank.

## Ambiente
WSL2 (Ubuntu 24.04), Python 3, Open MPI, Java 17.

## Como preparar
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt

## Como testar
Todos os comandos são rodados a partir da raiz do projeto.

    python -m pytest -q

## Como rodar
1. Gerar um grafo sintético (fica em `dados/`, fora do git):

       python -m src.comum.gerar_grafo --vertices 100000 --grau-medio 10 --saida dados/grafo_100k.npz

2. PageRank sequencial (versão de referência):

       python -m src.sequencial.pagerank --grafo dados/grafo_100k.npz

   Com `--tolerancia 0 --max-iteracoes 50` ele roda sempre 50 iterações,
   o que deixa as medições de tempo comparáveis entre as versões.