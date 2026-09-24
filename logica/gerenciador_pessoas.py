import json
import os
import uuid


class GerenciadorPessoas():
    def __init__(self, caminho_banco="dados/banco.json"):
        self.caminho_banco = caminho_banco
        self.pessoas = []
        self.carregar_dados()

    def carregar_dados(self):
        if not os.path.exists(self.caminho_banco):
            pasta = os.path.dirname(self.caminho_banco)
            if pasta and not os.path.exists(pasta):
                os.makedirs(pasta)
            self.pessoas = []
            self.salvar_dados()
            return
        try:
            with open(self.caminho_banco, "r", encoding="utf-8") as f:
                self.pessoas = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            self.pessoas = []

    def salvar_dados(self):
        pasta = os.path.dirname(self.caminho_banco)
        if pasta and not os.path.exists(pasta):
            os.makedirs(pasta)
        
        with open(self.caminho_banco, "w", encoding="utf-8") as f:
            json.dump(self.pessoas, f, ensure_ascii=False, indent=4)

    def _formatar_nome(self, nome):
        nome = nome.strip().title()
        return nome

    def listar_ordenado(self):
        lista_ordenada = sorted(self.pessoas, key=lambda p: p["nome"].lower())
        return lista_ordenada

    def buscar_por_inicial(self, letra):
        letra = letra.strip().upper()
        resultado = [p for p in self.listar_ordenado() if p["nome"].upper().startswith(letra)]
        return resultado

    def adicionar_pessoa(self, nome):
        nova_pessoa = {
            "id": str(uuid.uuid4()),
            "nome": self._formatar_nome(nome)
        }
        self.pessoas.append(nova_pessoa)
        self.salvar_dados()
        return nova_pessoa

    def editar_pessoa(self, id_pessoa, novo_nome):
        for pessoa in self.pessoas:
            if pessoa["id"] == id_pessoa:
                pessoa["nome"] = self._formatar_nome(novo_nome)
                self.salvar_dados()
                return True
        return False

    def remover_pessoa(self, id_pessoa):
        for pessoa in self.pessoas:
            if pessoa["id"] == id_pessoa:
                self.pessoas.remove(pessoa)
                self.salvar_dados()
                return True
        return False
