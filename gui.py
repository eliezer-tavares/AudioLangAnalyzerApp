import wx
import threading
from wx.lib.pubsub import pub
from core import AudioAnalyzer
import os

class AudioLangAnalyzerFrame(wx.Frame):
    """Interface gráfica principal da aplicação."""
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 400))
        self.panel = wx.Panel(self)
        self.analyzer = AudioAnalyzer()
        self.init_ui()
        self.bind_events()
        self.setup_accessibility()
        pub.subscribe(self.update_status, "status_update")
        pub.subscribe(self.on_analysis_complete, "analysis_complete")
        pub.subscribe(self.on_analysis_error, "analysis_error")

    def init_ui(self):
        """Inicializa os componentes da interface."""
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Botão para selecionar arquivo
        self.btn_select = wx.Button(self.panel, label="Selecionar Arquivo MP3")
        sizer.Add(self.btn_select, 0, wx.ALL | wx.EXPAND, 5)
        
        # Campo para mostrar arquivo selecionado
        self.txt_file = wx.TextCtrl(self.panel, style=wx.TE_READONLY)
        sizer.Add(self.txt_file, 0, wx.ALL | wx.EXPAND, 5)
        
        # Botão para iniciar análise
        self.btn_analyze = wx.Button(self.panel, label="Analisar Áudio")
        self.btn_analyze.Disable()
        sizer.Add(self.btn_analyze, 0, wx.ALL | wx.EXPAND, 5)
        
        # Área de status
        self.txt_status = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer.Add(self.txt_status, 1, wx.ALL | wx.EXPAND, 5)
        
        # Barra de progresso
        self.gauge = wx.Gauge(self.panel, range=100)
        sizer.Add(self.gauge, 0, wx.ALL | wx.EXPAND, 5)
        
        # Botão para salvar relatório
        self.btn_save = wx.Button(self.panel, label="Salvar Relatório PDF")
        self.btn_save.Disable()
        sizer.Add(self.btn_save, 0, wx.ALL | wx.EXPAND, 5)
        
        self.panel.SetSizer(sizer)

    def setup_accessibility(self):
        """Configura acessibilidade para leitores de tela."""
        for widget, name in [
            (self.btn_select, "Botão Selecionar Arquivo MP3"),
            (self.txt_file, "Caminho do Arquivo Selecionado"),
            (self.btn_analyze, "Botão Analisar Áudio"),
            (self.txt_status, "Log de Status"),
            (self.gauge, "Indicador de Progresso"),
            (self.btn_save, "Botão Salvar Relatório PDF")
        ]:
            acc = wx.Accessible(widget)
            acc.SetName(name)
            widget.SetAccessible(acc)

    def bind_events(self):
        """Associa eventos aos componentes."""
        self.btn_select.Bind(wx.EVT_BUTTON, self.on_select_file)
        self.btn_analyze.Bind(wx.EVT_BUTTON, self.on_analyze)
        self.btn_save.Bind(wx.EVT_BUTTON, self.on_save_report)

    def on_select_file(self, event):
        """Abre diálogo para selecionar arquivo MP3."""
        with wx.FileDialog(self, "Escolher arquivo MP3", wildcard="Arquivos MP3 (*.mp3)|*.mp3",
                         style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_OK:
                self.txt_file.SetValue(fileDialog.GetPath())
                self.btn_analyze.Enable()
                self.btn_save.Disable()

    def on_analyze(self, event):
        """Inicia a análise do áudio em uma thread separada."""
        self.btn_analyze.Disable()
        self.txt_status.Clear()
        self.gauge.Pulse()
        threading.Thread(target=self.analyzer.analyze, args=(self.txt_file.GetValue(),), daemon=True).start()

    def on_save_report(self, event):
        """Salva o relatório em PDF."""
        with wx.FileDialog(self, "Salvar Relatório PDF", wildcard="Arquivos PDF (*.pdf)|*.pdf",
                         style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_OK:
                self.analyzer.save_report(fileDialog.GetPath())
                wx.CallAfter(self.txt_status.AppendText, "Relatório salvo com sucesso.\n")

    def update_status(self, message):
        """Atualiza o texto de status na GUI."""
        wx.CallAfter(self.txt_status.AppendText, message + "\n")

    def on_analysis_complete(self):
        """Habilita botão de salvar após análise bem-sucedida."""
        wx.CallAfter(self.btn_save.Enable)
        wx.CallAfter(self.btn_analyze.Enable)
        wx.CallAfter(self.gauge.SetValue, 0)

    def on_analysis_error(self):
        """Reabilita controles após erro."""
        wx.CallAfter(self.btn_analyze.Enable)
      wx.CallAfter(self.gauge.SetValue, 0)
