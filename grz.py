import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = 'https://vin01.ru/index.php'
def avto_info(gos_number, url=URL):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    ids = {
        'input': 'num',
        'button': 'searchByGosNumberButton',
        'result': 'vinNumbers',
        'error': 'noMatchVin'
    }

    driver.get(url)
    time.sleep(5)
    driver.find_element(by=By.ID, value=ids['input']).send_keys(gos_number)
    driver.find_element(by=By.ID, value=ids['button']).click()
    time.sleep(5)
    children = driver.find_elements(by=By.ID, value=ids['result'])
    result = []
    if children:
        for child in children:
            result.append(child.text)
        return result
    else:
        return driver.find_element(by=By.ID, value=ids['error']).text



if __name__ == "__main__":
    GOSSES = ["А123АА71", "М999ОА71"]
    print(avto_info('А123АА71'))