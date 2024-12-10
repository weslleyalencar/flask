from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def get_cep(local):
    # Configurar o driver automaticamente
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Abrir uma página de exemplo
    driver.get("https://www.google.com/maps/search/"+ local)
    print(driver.title)

    driver.implicitly_wait(10)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    elementos = driver.find_elements(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[5]/div')

    print(elementos)


    # Fechar o navegador
    driver.quit()

    div_principal = soup.find_all('div', class_='Z8fK3b')
    lista = []
    for d in div_principal:
        nome = d.find('div', class_='NrDZNb').text if d.find('div', class_='NrDZNb') else "-"
        nota = d.find('div', class_='AJB7ye').text if d.find('div', class_='AJB7ye') else "-"
        telefone = d.find('span', class_='UsdlK').text if d.find('span', class_='UsdlK') else "-"
        categoria = d.find_all('div', class_='W4Efsd')[2].text.split("·")[0] if d.find_all('div', class_='W4Efsd')[2]  else "-"
        endereco = d.find_all('div', class_='W4Efsd')[2].text.split("·")[2] if d.find_all('div', class_='W4Efsd')[2] else "-"
        obj = {
            'nome': nome,
            'nota': nota,
            'categoria': categoria,
            'telefone': telefone,
            'endereco': endereco
        }
        lista.append(obj)

    # Fechar o navegador
    driver.quit()

    return lista

    



