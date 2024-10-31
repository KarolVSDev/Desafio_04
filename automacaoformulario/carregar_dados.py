from openpyxl import load_workbook
import pandas as pd

def carregar_dados(self):
    try:
        self.wb = load_workbook(self.excel_path)
        self.sheet = self.wb.active
        df = pd.read_excel(self.excel_path, engine='openpyxl')
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo Excel: {e}")
        return None
