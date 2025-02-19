import logging
from src.utility.open_driver import open_driver
from src.utility.helper_crawling import scroll_page_down
from src.datapipelines.DatapipelineToCSV import DatapipelineToCSV

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class ChototCrawler:
    def __init__(self):
        logging.info("ChototCrawler started")
        self.page = 1
        self.driver = open_driver()
        self.url = f"https://www.nhatot.com/thue-bat-dong-san-tp-ho-chi-minh?page={self.page}"
        self.data_pipeline = DatapipelineToCSV(file_name="data/nhatot.csv")

    def crawl(self):
        logging.info("Crawling Chotot...")
        # Crawling logic here
        while True:
            if self.page > 501:
                break
            self.driver.get(self.url)
            listings_container = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[@style='position:relative']")))
            scroll_page_down(self.driver)

            for listing in listings_container:
                self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", listing)
                time.sleep(1)
                name = type = price = size = url_img = place = poster = url = ""
                scraped_data = dict()
                try:
                    name = listing.find_element(By.XPATH, ".//h3").text
                    url_elem = listing.find_elements(By.XPATH, "./div/li/a")
                    if url_elem:
                        url = url_elem[0].get_attribute("href")
                    type_elems = listing.find_elements(By.XPATH, ".//span[@class='bwq0cbs tle2ik0']")
                    if type_elems:
                        type = type_elems[0].text
                    price_and_size_elem = listing.find_elements(By.XPATH, ".//div[@class='szp40s8 r9vw5if']/span")
                    if price_and_size_elem:
                        price = price_and_size_elem[0].text
                        size = price_and_size_elem[1].text

                    url_img_elem = listing.find_elements(By.XPATH, ".//img")
                    if url_img_elem:
                        url_img = url_img_elem[0].get_attribute("src")
                    place_elem = listing.find_elements(By.XPATH, ".//span[@class='c1u6gyxh tx5yyjc']")
                    if place_elem:
                        place = place_elem[0].text
                    poster_elem = listing.find_elements(By.XPATH, ".//span[@class='b2cylky s1amxne5']")
                    if poster_elem:
                        poster = poster_elem[0].text

                except Exception as e:
                    logging.error(f"Error: {e}")
                finally:
                    scraped_data["name"] = name
                    scraped_data["type"] = type
                    scraped_data["price"] = price
                    scraped_data["size"] = size
                    scraped_data["url_img"] = url_img
                    scraped_data["place"] = place
                    scraped_data["poster"] = poster
                    scraped_data["url"] = url
                    self.data_pipeline.add_data(scraped_data)
            
            self.page += 1  
            self.url = f"https://www.nhatot.com/thue-bat-dong-san-tp-ho-chi-minh?page={self.page}"
        # page_elem = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//div[@class='Paging_Paging__oREgP']")))
        
        self.data_pipeline.close_pipeline()
        logging.info("Crawling Chotot finished")