from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

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
    driver.get('https://www.zapimoveis.com.br/venda/casas/?pagina=1&transacao=Venda&tipoUnidade=Residencial,Casa&tipo=Im%C3%B3vel%20usado')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    time.sleep(random.randint(2, 5))

    print(driver.title)
finally:
    driver.quit()

anuncios = soup.select('li[data-cy="rp-property-cd"]')
df = []

for anuncio in anuncios:
    df.append({
        "link": anuncio.find('a').get('href') if anuncio.find('a') else None,
        "valor": anuncio.select_one('.text-2-25').get_text() if anuncio.select_one('.text-2-25') else None,
        "localizacao": anuncio.select_one('.text-2').get_text() if anuncio.select_one('.text-2') else None,
        "rua": anuncio.select_one('.l-text--weight-regular.truncate').get_text() if anuncio.select_one('.l-text--weight-regular.truncate') else None,
        "area": anuncio.select_one('.gap-0-5:nth-child(1)').get_text() if anuncio.select_one('.gap-0-5:nth-child(1)') else None,
        "quarto": anuncio.select_one('.gap-0-5:nth-child(2)').get_text() if anuncio.select_one('.gap-0-5:nth-child(2)') else None,
        "banheiros": anuncio.select_one('.gap-0-5:nth-child(3)').get_text() if anuncio.select_one('.gap-0-5:nth-child(3)') else None,
        "espaco_carros": anuncio.select_one('.gap-0-5:nth-child(4)').get_text() if anuncio.select_one('.gap-0-5:nth-child(4)') else None,
        "foto": anuncio.find('img', {'itemprop': 'image', 'loading': 'eager'}).get('src') if anuncio.find('img', {'itemprop': 'image', 'loading': 'eager'}) else None
    })

df = pd.DataFrame(df)
df = df.drop_duplicates(subset='link', keep='first')

df.to_excel('casas_encontradas.xlsx', index=False)
print(f"Dados exportados para Excel com sucesso. Total de {len(df)} registros únicos.")