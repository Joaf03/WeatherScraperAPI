from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scraper(url):
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

        weather_data = {}
        
        temperature = soup.find('div', class_='temperature')
        if temperature:
            weather_data['temperature'] = temperature.get_text(strip=True)
            
        # return {"message": str(soup)}
        return weather_data
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        driver.quit()