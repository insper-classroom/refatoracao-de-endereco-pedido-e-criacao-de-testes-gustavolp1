import pytest
import numpy as np
import requests
from classes.Endereco import Endereco

#requisito 1.1: FEITO
@pytest.mark.teste_generico
def test_cep_e_numero():
    endereco = Endereco('08320330', 430)
    assert endereco.cep == '08320330'
    assert endereco.numero == 430

#requisito 1.2: FEITO
@pytest.mark.teste_generico
def test_cep_int_ou_string():
    endereco = Endereco(8320330, 430)
    assert endereco.cep == '08320330'

#requisito 2.1: TODO

#requisito 2.2: TODO

#requisito 2.3 FEITO
def test_consulta_cep_sem_conexao():
    with pytest.raises(requests.exceptions.ConnectionError):
        Endereco.consultar_cep('08320330')