from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait          # Biblioteca usada para fazer o computador esperar
from selenium.webdriver.support import expected_conditions as EC # Biblioteca usada em conjunto com a WebDriverWait para a espera do computador ser mais dinâmica, essa biblioteca vai capturar as "condições esperadas" para poder prosseguir com o código



# Abaixo está sendo feito a coleta do Número do edital
def PegandoNumEdital(driver): 
    aguarde = WebDriverWait(driver, 300)
    edital = '//div[1]/ng-form/div[2]/p-h2/h2'
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, edital))) # Colocado essa ferramenta de espera para prevenir erro de carregamento no site 
    Edital = elemento.text
    return Edital


# Abaixo está sendo feita a coleta da Unidade gestora
def PegandoUnidadeGestora(driver):
    aguarde = WebDriverWait(driver, 300)
    unidgest = '//ng-form/div[3]/div/div/div/div/span'
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, unidgest)))
    Unidade_Gestora = elemento.text
    return Unidade_Gestora


# Abaixo está sendo feita a coleta da Descrição do objeto
def PegandoDescricaoObejeto(driver):
    aguarde = WebDriverWait(driver, 300)
    descobjeto = '//ng-form/div[6]/div/div/div/div/div/span' # descobjeto: Descrição do Objeto
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, descobjeto)))
    Descricao_Objeto = elemento.text
    return Descricao_Objeto


# Abaixo está sendo feita a coleta da Data de Emissão (refazer)
def PegandoDataEmissao(driver):
    aguarde = WebDriverWait(driver, 300)
    dataemissao = '//ng-form/div[8]/p-list/dl/ng-repeat[1]/dd'
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, dataemissao)))
    Data_Emissao = elemento.text
    return Data_Emissao


# Abaixo está sendo feita coleta do Prazo Final
def PegandoPrazoFinal(driver):
    aguarde = WebDriverWait(driver, 300)
    prazofinal = "//dt[contains(text(), 'Prazo final')]/following-sibling::dd"
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, prazofinal)))
    Prazo_Final = elemento.text
    return Prazo_Final


#Abaixo está sendo feita a coleta da Finalidade
def PegandoFinalidade(driver):
    aguarde = WebDriverWait(driver, 300)
    finalidade = '//ng-form/div[8]/p-list/dl/ng-repeat[2]/dd'
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, finalidade)))
    Finalidade = elemento.text
    return Finalidade


#Abaixo está sendo feita a coleta do Tipo
def PegandoTipo(driver):
    aguarde = WebDriverWait(driver, 300)
    tipo = '//ng-form/div[8]/p-list/dl/ng-repeat[3]/dd'
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, tipo)))
    Tipo = elemento.text
    return Tipo


#Abaixo está sendo feita a coleta da Forma de Julgamento(Global, Por Item, Lote)
def PegandoFormaJulgamento(driver):
    aguarde = WebDriverWait(driver, 300)
    formjulgamento = '//ng-form/div[8]/p-list/dl/ng-repeat[4]/dd'
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, formjulgamento)))
    Forma_Julgamento = elemento.text
    return Forma_Julgamento


#Abaico está sendo feita a coleta da Forma de Realização  
def PegandoFormaRealizacao(driver):
    aguarde = WebDriverWait(driver, 300)
    formrealizacao = '//ng-form/div[8]/p-list/dl/ng-repeat[5]/dd'
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, formrealizacao)))
    Forma_Realizacao = elemento.text
    return Forma_Realizacao


# Abaixo está sendo feita a coleta do Responsável Jurídico
def PegandoResponsavelJuridico(driver):
    aguarde = WebDriverWait(driver, 300)
    responsaveljuridico = "//dt[contains(text(), 'Responsável jurídico')]/following-sibling::dd"
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, responsaveljuridico)))
    Responsavel_Juridico = elemento.text
    return Responsavel_Juridico


# Abaixo está sendo feita a coleta do Valor estimado
def PegandoValorTotal(driver):
    aguarde = WebDriverWait(driver, 300)
    valortotal = "//dt[contains(text(), 'Valor total estimado')]/following-sibling::dd"
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, valortotal)))
    Valor_Total = elemento.text
    return Valor_Total


def pegando_informacoes(lista_avisos):
    driver = webdriver.Chrome('')
    return_info = []

    progresso_atual = 0
    for url, modalidade in lista_avisos:

        progresso_atual += 1
        print(progresso_atual, len(lista_avisos))

        driver.get(url)

        dicionario_linha = {
            "URL": url,
            "Numero do Edital": PegandoNumEdital(driver),
            "Modalidade": modalidade,
            "Unidade Gestora": PegandoUnidadeGestora(driver),
            "Descrição do Objeto": PegandoDescricaoObejeto(driver),
            "Data de Emissão": PegandoDataEmissao(driver),
            "Prazo Final": PegandoPrazoFinal(driver),
            "Finalidade": PegandoFinalidade(driver),
            "Tipo": PegandoTipo(driver),
            "Forma de Julgamento": PegandoFormaJulgamento(driver),
            "Forma de Realização": PegandoFormaRealizacao(driver),
            "Responsável Jurídico": PegandoResponsavelJuridico(driver),
            "Valor Total": PegandoValorTotal(driver)
        }

        return_info.append(dicionario_linha)

    driver.close()

    return return_info
