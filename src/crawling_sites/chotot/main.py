import logging
from src.crawling_sites.chotot.ChototCrawler import ChototCrawler

def main() -> None:
    chototcrawler = ChototCrawler()
    chototcrawler.crawl()