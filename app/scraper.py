from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from enum import Enum

class Day(Enum):
    NO = "Noroeste"
    NE = "Nordeste"
    SE = "Sudeste"
    SO = "Sudoeste"
    O = "Oeste"
    S = "Sul"
    N = "Norte"
    L = "Leste"

def scraper(url, date, city, region):
    # Configurar Chrome em modo headless para Docker
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        
        # Wait for the Javascript to load
        time.sleep(1)
        
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        weather_data = getWeatherData(soup, date, city, region)
        
        return weather_data
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        driver.quit()


def getWeatherData(soup, date, city, region):
    weather_data = {}

    dateDiv = soup.find('div', id=date)
    location = soup.find('h2', class_='local-header')

    # Needed because when the region is invalid, IPMA defaults the URL to Lisbon, Lisbon
    parameterLocation = f"{city}, {region}"

    if (not dateDiv or (location.get_text(strip=True) != parameterLocation)):
        raise Exception("Parâmetros inválidos: a data deve estar dentro dos próximos 9 dias e a localização tem de ser válida.")

    minTemp = dateDiv.find('span', class_='tempMin')
    maxTemp = dateDiv.find('span', class_='tempMax')
    windDir = dateDiv.find('div', class_='windDir')
    precProb = dateDiv.find('div', class_='precProb')

    elements = {
        'Data': date,
        'Localização': location,
        'Temperatura Mínima': minTemp,
        'Temperatura Máxima': maxTemp,
        'Direção do Vento': windDir,
        'Probabilidade de Precipitação': precProb
    }

    for key, element in elements.items():
        if element:
            if key == 'Direção do Vento':
                weather_data[key] = Day[element.get_text(strip=True)]
            elif key == 'Data':
                weather_data[key] = date
            else:
                weather_data[key] = element.get_text(strip=True)

    return weather_data