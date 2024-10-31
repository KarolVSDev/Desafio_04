from automacaoformulario import AutomacaoFormulario

excel_path = "funcionarios.xlsx"
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeQ12ubChFxcM6xhOEhzRc_f0C01Oojqbs0ibjOslAL_UgLmw/viewform"
automacao = AutomacaoFormulario(excel_path, form_url)
automacao.executar()
