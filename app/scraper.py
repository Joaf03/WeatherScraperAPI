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

def scraper(url, date):
    # Configurar Chrome em modo headless para Docker
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        
        time.sleep(2)
        
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        weather_data = getWeatherData(soup, date)
            
        return weather_data
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        driver.quit()


def getWeatherData(soup, date):
    weather_data = {}

    dateDiv = soup.find('div', id=date)
    location = soup.find('h2', class_='local-header')
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