
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Configuration des options Chrome
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    
    # Utilisation de webdriver-manager pour installer et gérer ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_inscription(driver):
    driver.get("https://inscription.it-akademy.fr/")
    driver.maximize_window()

    try:
        # Attendre que le bouton de cookies soit visible et cliquable
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK, tout accepter')]"))
        )
        cookie_button.click()
        print("Bannière des cookies fermée.")
    except Exception as e:
        print(f"Pas de bannière de cookies trouvée ou clic échoué : {str(e)}")
    
    # Remplir le formulaire d'inscription
    driver.find_element(By.XPATH,"//span[@class='text-itakademy']").click()
    driver.find_element(By.XPATH, "//input[@id='register-firstname']").send_keys("max")
    driver.find_element(By.ID, "register-lastname").send_keys("maxi")
    driver.find_element(By.ID, "register-email").send_keys("maxxi@gmail.com")
    driver.find_element(By.NAME, "phone").send_keys("0612345678")

    # Attendre que le bouton soit cliquable
    #submit_button = WebDriverWait(driver, 10).until(
     #   EC.element_to_be_clickable((By.CSS_SELECTOR, "#register-submit"))
    #)
    
    # Cliquer sur le bouton de soumission en utilisant JavaScript
    #driver.execute_script("arguments[0].click();", submit_button)

    time.sleep(5)  # Attendre 5 secondes pour observer le résultat avant de fermer le navigateur
    

