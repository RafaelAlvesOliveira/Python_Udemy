# type: ignore

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

from pathlib import Path
# from time import sleep
# import time
# import random
# import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import (
#     InvalidSessionIdException,
#     TimeoutException,
#     NoSuchElementException,
#     ElementNotInteractableException
# )

# Caminho da pasta raiz do projeto
ROOT_FOLDER = Path(__file__).parent


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--lang=en-US")  # Força inglês
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--auto-open-devtools-for-tabs")
    # Abre DevTools
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Win64; x64) Chrome/90.0.4430.212"
    )

    # Usando ChromeDriverManager para gerenciar automaticamente o driver
    service = ChromeService(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Script para evitar detecção
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """
    })

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    return driver


def search_google(driver, query):
    # Acessa o Google com parâmetros que forçam a versão nova
    driver.get("https://www.google.com/search?q=" + query + "&gl=us&hl=en")

    # Localiza os resultados - abordagem mais robusta
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
    )

    # Encontra todos os resultados (abordagem atualizada)
    results = driver.find_elements(By.CSS_SELECTOR, "div.g a h3")

    for idx, result in enumerate(results, 1):
        print(f"Resultado {idx}: {result.text}")
        print(f"Elemento completo: {result.get_attribute('outerHTML')}")

    return results


if __name__ == '__main__':
    try:
        driver = make_chrome_browser()

        # Pesquisa no Google
        search_term = "Hello World | Code.org"
        results = search_google(driver, search_term)

        # Mantém aberto para inspeção manual
        input("Pressione Enter para fechar...")

    except Exception as e:
        print(f"Erro: {str(e)}")
        driver.save_screenshot('error.png')
    finally:
        if 'driver' in locals():
            driver.quit()
