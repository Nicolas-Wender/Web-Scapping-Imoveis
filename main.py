from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
]

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": random.choice(user_agents)
})

try:
    # Navegação para o site alvo
    driver.get('https://www.zapimoveis.com.br/venda/casas/?pagina=1&transacao=Venda&tipoUnidade=Residencial,Casa&tipo=Im%C3%B3vel%20usado')
    
    # Pausa aleatória para simular comportamento humano
    time.sleep(random.randint(2, 5))
    
    # Captura do conteúdo HTML da página
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    print(driver.title)
    print("Número de elementos na página:", len(soup.select('*')))
    
finally:
    driver.quit()