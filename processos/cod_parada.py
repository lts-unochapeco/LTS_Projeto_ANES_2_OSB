from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def PegandocodParada():
    driver = webdriver.Chrome('')
    driver.get('https://transparencia.e-publica.net/epublica-portal/#/chapeco/portal/compras/licitacaoView?params=%7B%22id%22:%22MV8xMDU5OQ%3D%3D%22,%22mode%22:%22INFO%22%7D')
    aguarde = WebDriverWait(driver, 300)
    
    parada = '//*[@id="page-top"]/div[1]/div/portal-shell/section/div/div[2]/p'
    elemento = aguarde.until(EC.presence_of_element_located((By.XPATH, parada)))
    sleep(5)
    Parada = elemento.text
    driver.close()
    return Parada.strip()
