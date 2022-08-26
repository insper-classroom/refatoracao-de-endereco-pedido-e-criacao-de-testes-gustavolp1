import pytest
import numpy as np
from classes.Endereco import Endereco

@pytest.mark.op_simples
@pytest.mark.positivos
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    soma(v1, v2)
    assert 12 == soma(v1, v2)

@pytest.mark.op_simples
def test_soma_um_valor_positivo_um_negativo():
    v1 = 5.0
    v2 = -1.0
    soma(v1, v2)
    assert 4 == soma(v1, v2)

@pytest.mark.op_complexas
def test_media_lista_positivos():
    assert 2.5 == media_lista_valores([1, 2, 3, 4])

@pytest.mark.exercicio_1
def test_divisao_por_zero():
    v1 = 5.0
    v2 = 0.0
    assert np.inf == divisao(v1, v2)

@pytest.mark.exercicio_1
def test_media_valores_invalidos():
    assert 2 == media_lista_valores([1, 2, 3, 'a'])

@pytest.mark.exercicio_1
def test_media_lista_valores_vazia():
    assert 0 == media_lista_valores([])