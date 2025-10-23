from sqlite3 import Time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait          # Biblioteca usada para fazer o computador esperar
from selenium.webdriver.support import expected_conditions as EC # Biblioteca usada em conjunto com a WebDriverWait para a espera do computador ser mais dinâmica, essa biblioteca vai capturar as "condições esperadas" para poder prosseguir com o código.
from bs4 import BeautifulSoup

# Módulos personalizados:
from modulos.datetime import Time

def preparando_website():
    # 1 - Entrar no site
    driver = webdriver.Chrome('')
    driver.get('https://transparencia.e-publica.net/epublica-portal/#/chapeco/portal/compras/licitacaoTable')
    # Abaixo está a minha ferramenta de espera(substituindo o timesleep) criada.
    aguarde = WebDriverWait(driver, 10)

    # 2 - colocando o navegador em tela cheia
                   # abaixo eu coloquei como condição da minha ferramenta de espera o caminho XPATH do primeiro item a ser clicado
    aguarde.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div[4]/div/div[2]/div/div/div/div/a")))

    # selecionando o elemento situação na tela e clicando no mesmo (feito)
    situacao = driver.find_element(By.XPATH, "/html/body/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div[4]/div/div[2]/div/div/div/div/a")
    aguarde.until(EC.element_to_be_clickable(situacao))
    situacao.click()

    # Selecionando a opção "Aberta" e clicando nela (feito)
    situacao_clique = driver.find_element(By.XPATH, "/html/body/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div[4]/div/div[2]/div/div/div/div/div/ul/li[1]")
    aguarde.until(EC.element_to_be_clickable(situacao_clique))
    situacao_clique.click()

    # Selecionando o botão de consulta e clicando nele (feito)
    botao_consulta = driver.find_element(By.XPATH, "//*[@id='page-top']/div[1]/div/portal-shell/section/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div/button")
    botao_consulta.click()

    # 3 - Rolar para baixo e definir para mostrar 300 elementos na página (feito)
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
    data_atual = Time.get_now() # Obtém a data e hora atuais usando a função get_now() do módulo Time.

    html_source = driver.page_source # # Extrai o código-fonte HTML da página atual controlada pelo driver do Selenium.
    page_source = BeautifulSoup(html_source, 'html.parser') # Cria um objeto BeautifulSoup para facilitar a busca e extração de elementos HTML.
    noticias = page_source.findAll('tr', {'ng-repeat-start': '(rowIndex, row) in tableReq.rows'})

    lista_avisos = [] # Inicializa uma lista vazia para armazenar os avisos filtrados.

    # Itera sobre cada aviso encontrado na página.
    for aviso in noticias:

        # O valor é obtido de uma tag <span> dentro da quarta célula (<td> com índice 3).
        data_abertura_aviso = aviso.findAll('td')[3].findAll('div')[1].find('span').text

        # Se a data de abertura estiver vazia, o loop continua para o próximo aviso.
        if data_abertura_aviso == '':
            continue

        # Converte a string de data para um objeto datetime.
        data_abertura_aviso = Time.mudando_para_datetime(data_abertura_aviso)
        
        # Compara a data de abertura do aviso com a data atual. O código só prossegue se o aviso for atual ou futuro.
        if data_abertura_aviso >= data_atual:
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
    
    
def pegando_avisos_abertos():

    # Prepara o site para a raspagem (cliques, filtros, etc.).
    driver = preparando_website()

    # Obtém os links dos avisos da página.
    lista_avisos = pegando_links(driver)

    driver.close() # Fechando o navegador.

    # Registra o número de avisos abertos encontrados.
    return lista_avisos
