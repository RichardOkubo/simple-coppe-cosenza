"""Modelo Coppe-Cosenza simplificado (muito simples mesmo!) em Python.

Funções utilizadas: coppe_cosenza e cruzar.
"""

__version__ = "0.1.0"
__author__ = "Richard Okubo"

from functools import wraps
from typing import Callable, Dict, List, NewType


def validar(func: Callable) -> Callable:
    """Decorador para validar a oferta e a demanda."""
    Erro = NewType("Erro", Dict[str, str])
    erro: Erro = {
        "erro-1": "A oferta e a demanda devem ter a mesma dimensão.",
        "erro-2": "",
    }
    @wraps(func)
    def inner(oferta: List[str], demanda: List[str]) -> Callable:
        assert len(oferta) == len(demanda), erro["erro-1"]
        return func(oferta, demanda)

    return inner


def cruzar(index: int, n_fator: int,
           oferta: List[str], demanda: List[str]) -> float:
    """Função auxiliar.

    Cruzamento de oferta e demanda (com bonificação e penalização).
    """
    return {
        "cr": {
            "ex": 1.0,
            "bo": 1.0 - 1 / n_fator,
            "re": 1.0 - 2 / n_fator,
            "in": 1.0 - 3 / n_fator,
        }.get(oferta[index]),
        "co": {
            "ex": 1.0 + 1 / n_fator,
            "bo": 1.0,
            "re": 1.0 - 1 / n_fator,
            "in": 1.0 - 2 / n_fator,
        }.get(oferta[index]),
        "pc": {
            "ex": 1.0 + 2 / n_fator,
            "bo": 1.0 + 1 / n_fator,
            "re": 1.0,
            "in": 1.0 - 1 / n_fator,
        }.get(oferta[index]),
        "ir": {
            "ex": 1.0 + 3 / n_fator,
            "bo": 1.0 + 2 / n_fator,
            "re": 1.0 + 1 / n_fator,
            "in": 1.0,
        }.get(oferta[index]),
    }.get(demanda[index])


@validar
def coppe_cosenza(oferta: List[str], demanda: List[str]) -> List[float]:
    """Função principal para o modelo Coppe-Cosenza.

    LEGENDA:
        Avaliação dos fatores pela oferta:
            ex -> Excelente
            bo -> Bom
            re -> Regular
            in -> Insuficiente

        Grau de satisfação dos fatores pela demanda:
            cr -> Crucial
            co -> Condicionante
            pc -> Pouco condicionante
            ir -> Irrelevante

    EXEMPLO:
        >>> oferta_ = ['bo', 'ex', 'ex', 're', 'bo', 'ex', 'ex', 'in', 're']
        >>> demanda_ = ['cr', 'co', 'cr', 'pc', 'pc', 'co', 'co', 'pc', 'cr']
        >>> coppe_cosenza(oferta=oferta_, demanda=demanda_)
        ::: [0.8888888888888888, 1.1111111111111112, 1,
             1,                  1.1111111111111112, 1.1111111111111112,
             1.1111111111111112, 0.8888888888888888, 0.7777777777777778]
    """
    resultado: List[float] = list()
    n_fator: int = len(oferta)

    for i in range(n_fator):
        resultado.append(
            cruzar(index=i, n_fator=n_fator, oferta=oferta, demanda=demanda)
        )
    return resultado


if __name__ == "__main__":
    print(__doc__)
    
