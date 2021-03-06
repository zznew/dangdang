import scrapy
from ..items import DangdangbookItem


class DdbookPySpider(scrapy.Spider):
    name = 'ddbook'
    allowed_domains = ['http://search.dangdang.com']
    index = 1
    i = 0
    keywords = ['C语言', 'Python', 'Java', 'JavaScript', 'PHP', '算法', '数据库', '前端', '后端']
    start_urls = ['http://search.dangdang.com/?key={1}&page_index={2}'.format(keywords[i], index) for index in range(1, 100) for i in range(0, 8)]

    def parse(self, response):
        Book = DangdangbookItem()
        books = response.xpath('//*[@id="component_59"]/li')
        for book in books:
            Book['title'] = book.xpath('./p[1]/a/@title').extract_first()
            Book['detail'] = book.xpath('./p[2]/text()').extract_first()
            Book['price'] = book.xpath('./p[3]/span[1]/text()').extract_first()
            Book['comment'] = book.xpath('./p[4]/a/text()').extract_first()
            Book['label'] = book.xpath('./div[1]/span/span/text()').extract_first()
            Book['press'] = book.xpath('./p[5]/span[3]/a/text()').extract_first()
        yield Book
