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

3. PageRank com MPI (4 processos):

       mpirun -n 4 python -m mpi4py -m src.mpi.pagerank --grafo dados/grafo_100k.npz

   O `-m mpi4py` encerra todos os processos se um deles der erro, em vez
   de deixar os outros travados esperando.

4. PageRank com Spark (4 núcleos desta máquina):

       python -m src.spark.pagerank --grafo dados/grafo_100k.npz --master "local[4]"

   No cluster, troque o `--master` pelo endereço do mestre do Spark
   (ex.: `spark://<ip-do-mestre>:7077`).

## Como medir
O rodador executa uma versão várias vezes (3 por padrão), com 1, 2, 4...
processos e 50 iterações fixas, e anota cada execução em
`resultados/medicoes.csv`:

    python -m src.medicao.rodar --versao sequencial --grafo dados/grafo_1m.npz
    python -m src.medicao.rodar --versao mpi --grafo dados/grafo_1m.npz --processos 1 2 4 8
    python -m src.medicao.rodar --versao spark --grafo dados/grafo_1m.npz --processos 1 2 4 8

No cluster, use `--mpi-extra "--hostfile hosts --oversubscribe"` no MPI e
`--master spark://<ip-do-mestre>:7077` no Spark.

Depois, o analisador calcula tempo médio, speedup e eficiência:

    python -m src.medicao.analisar

- speedup = tempo com 1 processo ÷ tempo com p processos
- eficiência = speedup ÷ p (100% = cada processo rende o máximo possível)