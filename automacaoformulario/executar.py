import time

import time

def executar(self):
    if self.sheet is None:
        print("Erro ao carregar a planilha.")
        return

    for row in range(2, self.sheet.max_row + 1):
        status = self.sheet[f"I{row}"].value
        if status == "Pendente":
            nome = self.sheet[f"A{row}"].value
            genero = self.sheet[f"B{row}"].value
            email = self.sheet[f"C{row}"].value
            departamento = self.sheet[f"D{row}"].value
            endereco_texto = self.sheet[f"E{row}"].value
            cpf_texto = self.sheet[f"F{row}"].value
            rg_texto = self.sheet[f"G{row}"].value
            turno = self.sheet[f"H{row}"].value

            self.abrir_formulario()  
            self.preencher_formulario(nome, email, departamento, genero, turno, endereco_texto, cpf_texto, rg_texto)
            self.atualizar_status(row)
            time.sleep(1)
        else:
            print(f"Registro na linha {row} já foi cadastrado. Status: {status}")

    self.stop_browser()
