"""Funções de comparação usadas nos testes e nas medições."""

import numpy as np


def erro_l1(vetor_a: np.ndarray, vetor_b: np.ndarray) -> float:
    """
    Distância L1: soma das diferenças absolutas, posição por posição.
    É a nossa "régua" para dizer se dois PageRanks são iguais.
    """
    return float(np.abs(vetor_a - vetor_b).sum())