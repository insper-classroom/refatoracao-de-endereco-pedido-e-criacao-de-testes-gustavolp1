#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.__itens = {}

    def adicionar_item(self, item:Produto, qtd):
        
        id = item.get_id()
        
        # Implemente a adição do item no dicionário
        if id in self.__itens:
            self.__itens[id] += qtd
        else:
            self.__itens[id] = qtd
        

    def remover_item(self, item:Produto):
        id = item.get_id()
        if id in self.__itens:
            del self.__itens[id]
        # Implemente este método

    def __str__(self):
        return '{}'.format(self.__itens)
