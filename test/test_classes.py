import pytest
import numpy as np
from classes.Endereco import Endereco

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    soma(v1, v2)
    assert 12 == soma(v1, v2)