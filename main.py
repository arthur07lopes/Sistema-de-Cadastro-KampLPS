# Programa de gerenciamento de cadastro usando WXPython
# Autores: Arthur Santos Lopes e Gabriel Heineck Haberkamp.

import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 300))
        self.init_UI()

    def init_UI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        lbl_lista_cadastro = wx.StaticText(panel, label="&Lista de usuários cadastrados:")
        self.lista_cadastro = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.LC_SINGLE_SEL)
        vbox.Add(lbl_lista_cadastro, flag=wx.ALL, border=5)
        vbox.Add(self.lista_cadastro, flag=wx.EXPAND)
        # Grupo de radio buttons (wx.StaticBox) para seleção de ordem. Mais recentes ou ordem alfabética.
        static_box = wx.StaticBox(panel, label="Seleção de ordem de exibição")
        # Botões de opção
        radio_box = wx.BoxSizer(wx.VERTICAL)
        self.radio_ordem_alfabetica = wx.RadioButton(static_box, label="Ordem alfabética", style=wx.RB_GROUP)
        self.radio_mais_recentes = wx.RadioButton(static_box, label="Mais recentes")
        radio_box.Add(self.radio_ordem_alfabetica, flag=wx.ALL, border=5)
        radio_box.Add(self.radio_mais_recentes, flag=wx.ALL, border=5)
        static_box.SetSizer(radio_box)
        vbox.Add(static_box, flag=wx.ALL, border=5)
        # Botão para cadastrar novo usuário
        self.btn_cadastrar = wx.Button(panel, label="Cadastrar novo usuário")
        vbox.Add(self.btn_cadastrar, flag=wx.ALL, border=5)
        # Botão para editar cadastro (fica oculto por padrão)
        self.btn_editar_cadastro = wx.Button(panel, label="&Editar cadastro selecionado")
        self.btn_editar_cadastro.Hide()
        vbox.Add(self.btn_editar_cadastro, flag=wx.ALL, border=5)
        # Botão para remover o cadastro selecionado (fica oculto por padrão)
        self.btn_remover_cadastro = wx.Button(panel, label="&Remover cadastro selecionado")
        self.btn_remover_cadastro.Hide()
        vbox.Add(self.btn_remover_cadastro, flag=wx.ALL, border=5)
        # Campo para buscar usuários cadastrados
        lbl_busca = wx.StaticText(panel, label="&Buscar usuários")
        self.campo_busca = wx.TextCtrl(panel)
        vbox.Add(lbl_busca, flag=wx.ALL, border=5)
        vbox.Add(self.campo_busca, flag=wx.EXPAND)
        # Botão para sair do programa
        btn_sair = wx.Button(panel, label="&Sair do programa")
        btn_sair.Bind(wx.EVT_BUTTON, lambda event: self.Close())
        vbox.Add(btn_sair, flag=wx.ALL, border=5)
        panel.SetSizer(vbox)

app = wx.App()
frame = MainFrame(None, "Cadastro de usuários KampLPS")
frame.Show()
app.MainLoop()