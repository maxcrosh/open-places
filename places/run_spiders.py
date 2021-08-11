from scrapy.crawler import CrawlerProcess
from spiders.aparking import AparkingSpider

process = CrawlerProcess()

'''
Kazakhstan Spiders
'''
process.crawl(AparkingSpider)

process.start()