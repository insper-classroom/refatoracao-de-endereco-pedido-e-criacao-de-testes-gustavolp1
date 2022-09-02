#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    lista_clientes = []

    def __init__(self, id_produto, nome=''):
        self.id = id_produto
        self.nome = nome

    def set_id(self, id_novo):
        self.id = id_novo

    def get_id(self):
        return self.id

    def busca_nome(produto_id):
        for produto in Produto.lista_clientes:
            if produto.id == produto_id:
                return produto
        return None

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome}
