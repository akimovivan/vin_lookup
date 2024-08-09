import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from typing import Optional, List

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://vin01.ru/index.php'

def avto_info(gos_number: str, url: str = URL) -> Optional[List[str]]:
    """
    Retrieves information about a vehicle given its GOS number.

    Args:
        gos_number (str): The GOS number of the vehicle.
        url (str): The URL of the web page to scrape.

    Returns:
        Optional[List[str]]: A list of VIN numbers if found, None otherwise.
    """
    IDS = {
            'input': 'num',
            'button': 'searchByGosNumberButton',
            'result': 'vinNumbers',
            'error': 'noMatchVin'
        }
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    
    with webdriver.Firefox(options=options) as driver:
        driver.get(url)
        driver.find_element(by=By.ID, value=IDS['input']).send_keys(gos_number)
        driver.find_element(by=By.ID, value=IDS['button']).click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, IDS['result'])))
            children = driver.find_elements(by=By.ID, value=IDS['result'])
        except selenium.common.exceptions.TimeoutException:
            return None
        return [child.text for child in children] 


if __name__ == "__main__":
    GOSSES = ["А123АА71", "М999ОА71"]
    print(avto_info('А123АА71'))