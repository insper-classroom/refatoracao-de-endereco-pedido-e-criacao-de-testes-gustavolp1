#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re


class Pedido:
    EM_ABERTO = 1
    PAGO = 2
    
    def __init__(self, pessoa:PessoaFisica, endereco:Endereco, carrinho:Carrinho):
        self.pessoa = pessoa
        self.endereco = endereco
        self.carrinho = carrinho

    def __str__(self):
        return '{} - {} - {}'.format(self.pessoa, self.endereco, self.carrinho)
