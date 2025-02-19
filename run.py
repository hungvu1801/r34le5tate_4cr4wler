import logging
from src.crawling_sites.chotot.main import main
from src.utility.helper_crawling import create_directory
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
create_directory(f"log/{today}")

logging.basicConfig(
    filename=f"log/{today}/filelog.log",
	level=logging.INFO, 
	format="%(asctime)s: %(levelname)s : %(message)s ")


if __name__ == "__main__":
    main()