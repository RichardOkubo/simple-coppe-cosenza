
from pytest import fixture, mark

from coppe_cosenza import cruzar


@fixture
def fix():
    n_fator: int = 9
    oferta = ['bo', 'ex', 'ex', 're', 'bo', 'ex', 'ex', 'in', 're']
    demanda = ['cr', 'co', 'cr', 'pc', 'pc', 'co', 'co', 'pc', 'cr']
    return n_fator, oferta, demanda


@mark.parametrize("index, got", [
    (0, eval("1.0 - 1 / 9") ),
])
def test_cruzar(index, got, fix):
    print(fix)
    assert cruzar(index, *fix) == got
