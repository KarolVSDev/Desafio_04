from openpyxl import load_workbook
from botcity.web import WebBot, Browser
from webdriver_manager.chrome import ChromeDriverManager

from .carregar_dados import carregar_dados
from .abrir_formulario import abrir_formulario
from .preencher_formulario import preencher_formulario
from .atualizar_status import atualizar_status
from .executar import executar

class AutomacaoFormulario(WebBot):
    def __init__(self, excel_path, forms_url):
        super().__init__()
        self.excel_path = excel_path
        self.forms_url = forms_url
        self.wb = None
        self.sheet = None
        self.df = carregar_dados(self)
        self.driver_path = ChromeDriverManager().install()

    carregar_dados = carregar_dados
    abrir_formulario = abrir_formulario
    preencher_formulario = preencher_formulario
    atualizar_status = atualizar_status
    executar = executar
