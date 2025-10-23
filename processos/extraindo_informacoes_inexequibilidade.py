from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Biblioteca usada em conjunto com a WebDriverWait para a espera do computador ser mais dinâmica, essa biblioteca vai capturar as "condições esperadas" para poder prosseguir com o código
from bs4 import BeautifulSoup
from modulos.datetime import Time
# Abaixo está a minha ferramenta de espera(substituindo o timesleep) criada.

def preparando_site(driver, num):
    driver = webdriver.Chrome('')
    aguarde = WebDriverWait(driver, 10)

    driver.get('https://transparencia.e-publica.net/epublica-portal/#/chapeco/portal/compras/licitacaoTable')
    aguarde.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div[4]/div/div[2]/div/div/div/div/a")))

    aguarde.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div")))
    botao_data = driver.find_element(By.XPATH, "/html/body/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div")
    aguarde.until(EC.element_to_be_clickable(botao_data))
    botao_data.click()

    data_inicio_ano = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/input")
    aguarde.until(EC.element_to_be_clickable(data_inicio_ano))
    data_inicio_ano.click()
    data_inicio_ano.clear()
    data_inicio_ano.send_keys(f"01/01/{Time.pegando_lista_atual()[0]}")

    botao = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/button[1]")
    botao.click()

    # selecionando o elemento modalidade na tela e clicando no mesmo (feito)
    modalidade = driver.find_element(By.XPATH, "/html/body/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/a")
    aguarde.until(EC.element_to_be_clickable(modalidade))
    modalidade.click()

    # Selecionando a opção "Dispensa" e clicando nela (feito)
    modalidade_clique = driver.find_element(By.XPATH, "/html/body/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div/div/ul/li["+num+"]")
    aguarde.until(EC.element_to_be_clickable(modalidade_clique))
    modalidade_clique.click()

    # Selecionando o botão de consulta e clicando nele (feito)
    botao_consulta = driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div/button")
    botao_consulta.click()

    # Rolar para baixo e definir para mostrar 300 elementos na página (feito)
    botao_elementos = driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[3]/div[1]/div/div/div/a/div/b")
    aguarde.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='page-top']/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[3]/div[1]/div/div/div/a/div/b")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", 
                        botao_elementos)

    # Fazendo uma pausa no programa para o mesmo continuar após o botão aparecer na tela.
    aguarde.until(EC.element_to_be_clickable(botao_elementos))
    botao_elementos.click()

    # Selecionando e clicando na opção de 300 elementos.
    botao_opcao_300 = driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[3]/div[1]/div/div/div/div/ul/li[4]")
    botao_opcao_300.click() # Executando a função de click.

    return driver


def pegando_links(driver):
    html_source = driver.page_source # # Extrai o código-fonte HTML da página atual controlada pelo driver do Selenium.
    page_source = BeautifulSoup(html_source, 'html.parser') # Cria um objeto BeautifulSoup para facilitar a busca e extração de elementos HTML.
    noticias = page_source.findAll('tr', {'ng-repeat-start': '(rowIndex, row) in tableReq.rows'})

    lista_avisos = [] # Inicializa uma lista vazia para armazenar os avisos filtrados.

    # Itera sobre cada aviso encontrado na página.
    for aviso in noticias:
        # Extrai a URL do aviso, navegando pela estrutura HTML até o atributo 'href'.
        aviso_url = aviso.findAll('td')[6] \
                                .find('p-actions').find('div') \
                                .findAll('ng-repeat')[1] \
                                .find('a')['href']

        # Extrai a modalidade do aviso da segunda célula (<td> com índice 1).
        modalidade = aviso.findAll('td')[1].findAll('div')[1].find('span').get_text()

        # Define a URL base do site.
        base_url = "https://transparencia.e-publica.net/epublica-portal/"

        # Adiciona a URL completa e a modalidade à lista de avisos.
        lista_avisos.append([str(base_url) + aviso_url, modalidade])

    return lista_avisos


def pegando_avisos_inexequibilidades():
    driver = webdriver.Chrome('')
    
    num = "5"
    c = 0
    while True:
        driver = preparando_site(driver, num)

        if c == 0:
            lista_aviso0 = pegando_links(driver)
            driver.close()
        else:
            lista_aviso1 = pegando_links(driver)

        num = "7"
        c += 1
        if c == 2:
            break
        

    driver.close()
    lista_avisos = lista_aviso0 + lista_aviso1

    return lista_avisos