

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configuration des options Chrome pour désactiver la popup de sélection du moteur de recherche
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
import time

#chrome_options.add_argument("--disable-popup-blocking")# pour bloquer les popups

import time
# Initialiser le navigateur
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://inscription.it-akademy.fr/")

driver.delete_all_cookies()

driver.maximize_window()

try:
    cookie_button = driver.find_element(By.XPATH, "//button[contains(text(), 'OK, tout accepter')]")
    cookie_button.click()
    print("Bannière des cookies fermée.")
except:
    print("Pas de bannière de cookies trouvée ou clic échoué.")

driver.find_element(By.CLASS_NAME,"text-itakademy").click()
driver.find_element(By.XPATH,"//input[@id='register-firstname']").send_keys("max")
driver.find_element(By.ID,"register-lastname").send_keys("maxi")
driver.find_element(By.ID,"register-email").send_keys("maxiip@gmail.com")
driver.find_element(By.NAME,"phone").send_keys("0612345678")
driver.find_element(By.CSS_SELECTOR,"#register-submit").click()

time.sleep(3)   

if driver.title== "Espace candidats | ERP IT-Akademy":
    print("Inscription réussie")

else:
    print("Inscription échouée")

driver.quit()




