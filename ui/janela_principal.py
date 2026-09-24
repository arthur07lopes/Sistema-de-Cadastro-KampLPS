import wx
from .dialogos import DialogoPessoa

COR_FUNDO = wx.Colour(20, 20, 22) # preto
COR_PAINEL = wx.Colour(30, 30, 33) # cinza com tom escuro
COR_DESTAQUE = wx.Colour(255, 30, 30) # vermelho em neon
COR_TEXTO = wx.Colour(230, 230, 230) # cinza claro, quase branco

class JanelaPrincipal(wx.Frame):
    def __init__(self, gerenciador):
        super().__init__(parent=None, title="Sistema de Cadastro KampLPS", size=(650, 480))
        self.gerenciador = gerenciador
        self.SetBackgroundColour(COR_FUNDO)

        painel = wx.Panel(self)
        painel.SetBackgroundColour(COR_FUNDO)

        label_busca = wx.StaticText(painel, label="&Buscar por Letra:")
        label_busca.SetForegroundColour(COR_TEXTO)

        self.campo_busca = wx.TextCtrl(painel)
        self.campo_busca.SetName("Campo de busca por inicial do nome")

        btn_buscar = wx.Button(painel, label="&Buscar")
        btn_buscar.SetName("Botão Buscar")
        btn_buscar.Bind(wx.EVT_BUTTON, self.ao_clicar_buscar)

        lbl_lista = wx.StaticText(painel, label="&Lista de pessoas cadastradas:")
        
        self.lista = wx.ListCtrl(painel, style=wx.LC_REPORT)
        self.lista.InsertColumn(0, "Nome", width=400)
        self.lista.SetName("Lista de pessoas cadastradas")

        btn_adicionar = wx.Button(painel, label="&Adicionar")
        btn_adicionar.SetName("Botão adicionar pessoa")
        btn_adicionar.Bind(wx.EVT_BUTTON, self.ao_clicar_adicionar)

        btn_editar = wx.Button(painel, label="&Editar")
        btn_editar.SetName("Botão editar pessoa selecionada")
        btn_editar.Bind(wx.EVT_BUTTON, self.ao_clicar_editar)

        btn_remover = wx.Button(painel, label="&Remover")
        btn_remover.SetName("Botão remover pessoa selecionada")
        btn_remover.Bind(wx.EVT_BUTTON, self.ao_clicar_remover)

        sizer_busca = wx.BoxSizer(wx.HORIZONTAL)
        sizer_busca.Add(label_busca, 0, wx.ALL | wx.CENTER, 5)
        sizer_busca.Add(self.campo_busca, 1, wx.ALL | wx.EXPAND, 5)
        sizer_busca.Add(btn_buscar, 0, wx.ALL, 5)

        sizer_botoes = wx.BoxSizer(wx.HORIZONTAL)
        sizer_botoes.Add(btn_adicionar, 0, wx.ALL, 5)
        sizer_botoes.Add(btn_editar, 0, wx.ALL, 5)
        sizer_botoes.Add(btn_remover, 0, wx.ALL, 5)
        
        sizer_lista = wx.BoxSizer(wx.VERTICAL)
        sizer_lista.Add(lbl_lista, 0, wx.ALL, 5)
        sizer_lista.Add(self.lista, 1, wx.ALL | wx.EXPAND, 5)
        

        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        sizer_principal.Add(sizer_busca, 0, wx.EXPAND)
        sizer_principal.Add(sizer_lista, 1, wx.EXPAND | wx.ALL, 10)
        sizer_principal.Add(sizer_botoes, 0, wx.CENTER)

        painel.SetSizer(sizer_principal)
        self.Centre()
        self.atualizar_lista(self.gerenciador.listar_ordenado())

    def atualizar_lista(self, pessoas):
        self.lista.DeleteAllItems()
        self.pessoas_exibidas = pessoas
        for pessoa in pessoas:
            self.lista.InsertItem(self.lista.GetItemCount(), pessoa["nome"])
    def ao_clicar_buscar(self, evento):
        letra = self.campo_busca.GetValue()
        if letra.strip() == "":
            self.atualizar_lista(self.gerenciador.listar_ordenado())
        else:
            self.atualizar_lista(self.gerenciador.buscar_por_inicial(letra))

    def ao_clicar_adicionar(self, evento):
        dialogo = DialogoPessoa(titulo="Adicionar pessoa")
        if dialogo.ShowModal() == wx.ID_OK:
            nome = dialogo.obter_nome()
            if nome.strip() != "":
                self.gerenciador.adicionar_pessoa(nome)
                self.atualizar_lista(self.gerenciador.listar_ordenado())
        dialogo.Destroy()

    def ao_clicar_editar(self, evento):
        indice = self.lista.GetFirstSelected()
        if indice == -1:
            wx.MessageBox("Selecione uma pessoa na lista primeiro.", "Aviso")
            return
        pessoa = self.pessoas_exibidas[indice]
        dialogo = DialogoPessoa(
            titulo="Editar pessoa", nome_inicial=pessoa["nome"]
        )
        if dialogo.ShowModal() == wx.ID_OK:
            novo_nome = dialogo.obter_nome()
            if novo_nome.strip() != "":
                self.gerenciador.editar_pessoa(pessoa["id"], novo_nome)
                self.atualizar_lista(self.gerenciador.listar_ordenado())
        dialogo.Destroy()

    def ao_clicar_remover(self, evento):
        indice = self.lista.GetFirstSelected()
        if indice == -1:
            wx.MessageBox("Selecione uma pessoa na lista primeiro.", "Aviso")
            return

        pessoa = self.pessoas_exibidas[indice]
        confirmar = wx.MessageBox(
            f"Remover {pessoa['nome']}?", "Confirmar remoção",
            wx.YES_NO | wx.ICON_QUESTION
        )
        if confirmar == wx.YES:
            self.gerenciador.remover_pessoa(pessoa["id"])
            self.atualizar_lista(self.gerenciador.listar_ordenado())
