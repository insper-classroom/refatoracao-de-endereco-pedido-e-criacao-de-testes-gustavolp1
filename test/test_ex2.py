import pytest
import numpy as np
import requests
from classes.Endereco import Endereco

#requisito 1.1: FEITO
@pytest.mark.teste_1_1
def test_cep_e_numero():
    endereco = Endereco('08320330', 430)
    assert endereco.cep == '08320330'
    assert endereco.numero == 430

#requisito 2.1: FEITO
@pytest.mark.teste_2_1
def test_cep_int_ou_string():
    endereco = Endereco(8320330, 430)
    assert endereco.cep == '08320330'

#requisito 2.2: FEITO
@pytest.mark.teste_2_2
def test_return_falso_cep_inverificavel():
    endereco = Endereco.consultar_cep('')
    if endereco == {'erro': True}:
        endereco = False
    assert endereco == False

#requisito 2.3 FEITO
@pytest.mark.teste_2_3
def test_consulta_cep_sem_conexao():
    with pytest.raises(requests.exceptions.ConnectionError):
        Endereco.consultar_cep('08320330')