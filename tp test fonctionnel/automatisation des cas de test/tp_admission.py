

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
import time

#chrome_options.add_argument("--disable-popup-blocking")# pour bloquer les popups

import time
# Initialiser le navigateur
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://inscription.it-akademy.fr/")

driver.maximize_window()

try:
    cookie_button = driver.find_element(By.XPATH, "//button[contains(text(), 'OK, tout accepter')]")
    cookie_button.click()
    print("Bannière des cookies fermée.")
except:
    print("Pas de bannière de cookies trouvée ou clic échoué.")
    
email= driver.find_element(By.XPATH,"//input[@placeholder='Identifiant (e-mail)']")

email.send_keys("esmailhaidari24@gmail.com")

passowrd= driver.find_element(By.XPATH,"//input[@placeholder='Mot de passe']")

passowrd.send_keys("kGGif46h")

time.sleep(3)
button= driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(4) > form.login-form > div.form-actions > button")
button.click()
 
if driver.title== "ERP IT-Akademy": 
    print("Connexion réussie")
else:
    print("Connexion échouée")
driver.close()
     


