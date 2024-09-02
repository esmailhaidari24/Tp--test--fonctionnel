
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
def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")

    # Installer la version correcte de ChromeDriver
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    
    yield driver  # retourne le driver pour être utilisé dans le test
    
    # Fermeture du navigateur après le test
    driver.quit()

def test_login(setup_browser):
    driver = setup_browser
    
    # Ouvrir la page
    driver.get("https://inscription.it-akademy.fr/")

    try:
        # Attendre que le bouton de cookies soit visible et cliquable
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK, tout accepter')]"))
        )
        cookie_button.click()
        print("Bannière des cookies fermée.")
    except Exception as e:
        print(f"Pas de bannière de cookies trouvée ou clic échoué : {str(e)}")
    
    # Saisie des informations de connexion
    email = driver.find_element(By.XPATH, "//input[@placeholder='Identifiant (e-mail)']")
    password = driver.find_element(By.XPATH, "//input[@placeholder='Mot de passe']")
    
    email.send_keys("esmailhaidari24@gmail.com")
    password.send_keys("kGGif46h")
    
    time.sleep(3)
    
    # Cliquez sur le bouton de connexion
    button = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(4) > form.login-form > div.form-actions > button")
    button.click()
    
    time.sleep(3)