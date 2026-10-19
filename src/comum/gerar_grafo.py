"""
Gera um grafo sintético e salva em disco.

Uso (a partir da raiz do projeto):
    python -m src.comum.gerar_grafo --vertices 100000 --grau-medio 10 \
        --saida dados/grafo_100k.npz
"""

import argparse
import time

from src.comum.grafo import gerar_grafo_aleatorio, salvar_grafo


def main() -> None:
    parser = argparse.ArgumentParser(description="Gerador de grafos sintéticos")
    parser.add_argument("--vertices", type=int, required=True, help="número de páginas")
    parser.add_argument("--grau-medio", type=float, default=10.0, help="links por página (média)")
    parser.add_argument("--semente", type=int, default=42, help="semente aleatória")
    parser.add_argument("--saida", type=str, required=True, help="arquivo .npz de saída")
    args = parser.parse_args()

    inicio = time.perf_counter()
    grafo = gerar_grafo_aleatorio(args.vertices, args.grau_medio, args.semente)
    salvar_grafo(grafo, args.saida)
    duracao = time.perf_counter() - inicio

    sem_saida = int((grafo.grau_saida() == 0).sum())
    print(f"Grafo salvo em {args.saida}")
    print(f"  vértices: {grafo.n_vertices}")
    print(f"  arestas: {grafo.n_arestas}")
    print(f"  páginas sem links de saída: {sem_saida}")
    print(f"  tempo: {duracao:.2f} s")


if __name__ == "__main__":
    main()