import os
from peewee import *
from flask import Flask, json, jsonify
from playhouse.shortcuts import model_to_dict

arq = 'many−to−many−com−lista.db'
db = SqliteDatabase (arq)

class BaseModel(Model):
    class Meta:
        database = db

class Produto(BaseModel):
    nome_produto = CharField()
    valor = CharField()
    cod_id = CharField()
class Fornecedor(BaseModel):
    nome = CharField()
    telefone = CharField()
    tipo_produto = CharField() 

class Cliente(BaseModel):
    nome = CharField()
    cpf = CharField()

class Carrinho(BaseModel):
    produto = ForeignKeyField(Produto)
    quantidade = IntegerField()

class Caixa(BaseModel):
    produto = ForeignKeyField(Produto)
    carrinho = ForeignKeyField(Carrinho)
    cliente = ForeignKeyField(Cliente)

class Historico_vendas(BaseModel):
    caixa = ForeignKeyField(Caixa)
    data = CharField()
    cliente = ForeignKeyField(Cliente)


class Funcionario(BaseModel):
    nome = CharField()
    turno = CharField()
    cpf = CharField()

class Setor(BaseModel):
    nome_setor = CharField()

class Estoque(BaseModel):
    produto = ForeignKeyField(Produto)
    fornecedor = ForeignKeyField(Fornecedor)
    quantidade = IntegerField()

class Mercado(BaseModel):
    nome = CharField()
    setor = ForeignKeyField(Setor)
    funcionario = ForeignKeyField(Funcionario)


if __name__ == "__main__":
    db.connect()
    db.create_tables([Produto, Fornecedor , Cliente, Carrinho, Caixa, Historico_vendas, Funcionario, Setor , Estoque, Mercado])

    
    produto1 = Produto.create(nome_produto = "maca",cod_id = "123" , valor = "2.50")
    fornecedor1 = Fornecedor.create(nome = "Zenon Frutas", telefone = "33445566", tipo_produto = "Fruta")
    cliente1 = Cliente.create(nome = "Gabriel Rosa", cpf = "234567890-09")
    carrinho1 = Carrinho.create(produto = produto1, quantidade = 4)
    caixa1 = Caixa.create(produto = produto1, carrinho = carrinho1, cliente = cliente1)
    historico_vendas1 = Historico_vendas.create(caixa = caixa1, data = "20/04/19", cliente = cliente1)
    funcionario1 = Funcionario.create(nome = "Rose Mel", turno = "matutino", cpf = "234156789-09")
    setor1 = Setor.create(nome_setor = "Limpeza")
    estoque1 = Estoque.create(produto = produto1, fornecedor = fornecedor1, quantidade = 100)
    mercado1 = Mercado.create(nome = "Rede Top", setor = setor1, funcionario = funcionario1)
    
    json = list(map(model_to_dict, Produto.select()))

    print(produto1.nome_produto)
