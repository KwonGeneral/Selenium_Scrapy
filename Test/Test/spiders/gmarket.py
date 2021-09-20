
import scrapy

from Test.items import TestItem


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'  # 크롤러(spider) 이름
    allowed_domains = ['https://corners.gmarket.co.kr/Bestsellers/']  # 허용된 주소
    start_urls = ['https://corners.gmarket.co.kr/Bestsellers/']  # 크롤링할 페이지 주소, 여러개 작성 가능 ['첫번째', '두번째' ...]

    def parse(self, response):  # 크롤링 결과가 response 매개변수에 담겨져서 옴.
        # print(response.text)
        titles = response.css('div.best-list li > a::text').getall()
        prices = response.css('div.best-list ul li div.item_price div.s-price strong span::text').getall()

        try:
            for i in range(len(titles)):
                item = TestItem()
                item['title'] = titles[i]
                item['price'] = int(prices[i].replace("원", "").replace(",", ""))
                yield item
        except IndexError:
            return

        # for num, title in enumerate(titles):
        #     item = TestItem()
        #     item['title'] = title
        #     item['price'] = prices
        #     yield item




