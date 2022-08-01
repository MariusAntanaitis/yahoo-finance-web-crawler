import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# EXAMPLES

# elem.send_keys("pycon") // send keyboard inputs
# elem.send_keys(Keys.RETURN) // press Enter
# .click() // mouse click on element

# agree_button = driver.find_element(By.NAME, "agree") // selecting elements By: ID, NAME, CLASS


def lets_go_power_rangers():
    """Power Rangers smash yahoo finance"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://finance.yahoo.com")

    agree_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "agree")))

    agree_button.click()

    time.sleep(3)

    navbar = driver.find_element(By.ID, "Nav-0-DesktopNav-0-DesktopNav")
    textas = navbar.find_elements(By.TAG_NAME, "a")[0].get_attribute("innerText")

    print(textas)

    driver.close()


lets_go_power_rangers()
