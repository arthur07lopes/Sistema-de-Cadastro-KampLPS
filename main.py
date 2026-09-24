import wx

from logica.gerenciador_pessoas import GerenciadorPessoas
from ui.janela_principal import JanelaPrincipal

if __name__ == "__main__":
  app = wx.App()
  gerenciador = GerenciadorPessoas()
  janela = JanelaPrincipal(gerenciador)
  janela.Show()
  app.MainLoop()
