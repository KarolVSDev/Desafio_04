def atualizar_status(self, linha):
    self.sheet[f"I{linha}"].value = "Cadastrado"
    self.wb.save(self.excel_path)
