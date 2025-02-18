import logging
from src.crawling_sites.chotot.ChototCrawler import ChototCrawler

async def main() -> None:
    chototcrawler = ChototCrawler()
    await chototcrawler.crawl()