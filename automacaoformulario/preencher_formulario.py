import time
from botcity.web import By

def preencher_formulario(self, nome, email, departamento, genero, turno, endereco_texto, cpf_texto, rg_texto):
    # Campo Nome
    input_nome = self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH)
    input_nome.click()
    time.sleep(1)
    input_nome.send_keys(nome)
    time.sleep(1)

    # Campo Gênero
    if genero.lower() in ["feminino", "f"]:
        genero_feminino = self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div', By.XPATH)
        genero_feminino.click()
    else:
        genero_masculino = self.find_element('//*[@id="i9"]/div[3]/div', By.XPATH)
        genero_masculino.click()
    time.sleep(1)

    # Campo Email
    email_input = self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH)
    email_input.click()
    time.sleep(1)
    email_input.send_keys(email)
    time.sleep(1)

    # Campo Departamento
    departamento_input = self.find_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH)
    departamento_input.click()
    time.sleep(1)
    departamento_input.send_keys(departamento)
    time.sleep(1)

    # Campo Endereço
    endereco_input = self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea', By.XPATH)
    endereco_input.click()
    time.sleep(1)
    endereco_input.send_keys(endereco_texto)

    # Campo CPF
    cpf_input = self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH)
    cpf_input.click()
    time.sleep(1)
    cpf_input.send_keys(cpf_texto)

    # Campo RG
    rg_input = self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH)
    rg_input.click()
    time.sleep(1)
    rg_input.send_keys(rg_texto)

    # Campo Turno
    if turno.lower() == "primeiro":
        turno = self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div', By.XPATH)
        turno.click()
    elif turno.lower() == "segundo":
        turno = self.find_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div', By.XPATH)
        turno.click()
    else:
        turno = self.find_element('/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[3]/label/div', By.XPATH)
        turno.click()
    time.sleep(1)

    # Botão Enviar
    enviar_btn = self.find_element('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span', By.XPATH)
    enviar_btn.click()
    time.sleep(2)
