import json
import os
import uuid


class GerenciadorPessoas():
    def __init__(self, caminho_banco="dados/banco.json"):
        self.caminho_banco = caminho_banco
        self.pessoas = []
        self.carregar_dados()

    def carregar_dados(self):
        if not os.path.exists(self.caminho_banco)
        