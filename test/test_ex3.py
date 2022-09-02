import pytest
import numpy as np
import requests
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento

@pytest.mark.produto
def test_produto():
    produto = Produto("0010342967", "Sabonete")
    assert produto.id == "0010342967"
    assert produto.nome == "Sabonete"

@pytest.mark.pessoafisica
def test_pessoafisica():
    pessoa = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    assert pessoa.nome == 'Carlos'
    assert pessoa.email == 'tiago@email.com'
    assert pessoa.cpf == '524.222.452-6'

@pytest.mark.carrinho
def test_carrinho():
    sabonete = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete, 2)
    assert carrinho.itens == {'0010342967': 2}

@pytest.mark.pedidos
def test_pedidos():
    pessoa = 'Carlos'
    endereco = 'Rua Clemente Falcão'
    carrinho = Carrinho()
    pedido = Pedido(pessoa, endereco, carrinho)
    assert pedido.pessoa == pessoa
    assert pedido.endereco == endereco
    assert pedido.carrinho == carrinho