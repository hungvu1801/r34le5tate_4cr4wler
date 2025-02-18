import logging
from src.utility.open_driver import open_driver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChototCrawler:
    def __init__(self):
        logging.info("ChototCrawler started")
        self.driver = open_driver()
        self.url = "https://www.nhatot.com/thue-bat-dong-san-tp-ho-chi-minh"

    def crawl(self):
        logging.info("Crawling Chotot...")
        # Crawling logic here
        self.driver.get(self.url)
        listings_container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@style='position: relative;']")))
        for listing in listings_container:
            
                
        logging.info("Crawling Chotot finished")