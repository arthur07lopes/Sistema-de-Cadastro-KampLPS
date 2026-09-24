import wx

class DialogoPessoa(wx.Dialog):
    def __init__(self, titulo, nome_inicial=""):
        super().__init__(None, title=titulo, size=(350, 150))
        self.SetBackgroundColour(wx.Colour(30, 30, 33))

        painel = wx.Panel(self)
        painel.SetBackgroundColour(wx.Colour(30, 30, 33))

        label = wx.StaticText(painel, label="Nome:")
        label.SetForegroundColour(wx.Colour(230, 230, 230))

        self.campo_nome = wx.TextCtrl(painel, value=nome_inicial)
        self.campo_nome.SetName("Campo nome da pessoa")

        btn_ok = wx.Button(painel, wx.ID_OK, label="&Salvar")
        btn_ok.SetName("Botão salvar")
        btn_cancelar = wx.Button(painel, wx. ID_CANCEL, label="&Cancelar")
        btn_cancelar.SetName("Botão cancelar")

        sizer_botoes = wx.BoxSizer(wx.HORIZONTAL)
        sizer_botoes.Add(btn_ok, 0, wx.ALL, 5)
        sizer_botoes.Add(btn_cancelar, 0, wx.ALL, 5)

        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        sizer_principal.Add(label, 0, wx.ALL, 10)
        sizer_principal.Add(self.campo_nome, 0, wx.ALL | wx.EXPAND, 10)
        sizer_principal.Add(sizer_botoes, 0, wx.CENTER)

        painel.SetSizer(sizer_principal)

    def obter_nome(self):
        return self.campo_nome.GetValue()
        
