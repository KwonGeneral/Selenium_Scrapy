
import scrapy
from Test.items import CategoryItem


class GmarketCategorySpider(scrapy.Spider):
    name = "gmarket_category"

    # allowed_domains = ['https://corners.gmarket.co.kr/Bestsellers']
    # start_urls = ['https://corners.gmarket.co.kr/Bestsellers']

    # 자동으로 카테고리 url들을 크롤링해서 비동기로 추출해서 가져오기 위해서 사용
    def start_requests(self):
        yield scrapy.Request(url="https://corners.gmarket.co.kr/Bestsellers", callback=self.parse)

        # 참고로, 여러개의 start_requests 작성이 가능함
        # yield scrapy.Request(url="두 번째 링크", callback=self.parse_second)

    # def parse_second(self, response, **kwargs):
    #     pass

    def parse(self, response, **kwargs):
        print("-- parse 함수 --")
        main_category_links = response.css('div.gbest-cate ul.by-group li a::attr(href)').getall()
        main_category_names = response.css('div.gbest-cate ul.by-group li a::text').getall()

        # 1) 메인 카테고리 크롤링
        for index, category_link in enumerate(main_category_links):
            # print("https://corners.gmarket.co.kr" + category_link, category_names[index])

            # 카테고리 링크 안에 상세 링크들을 가져오기 위해서 scrapy.Request 사용. (재귀함수 라고 생각하면 될듯)
            # 값 전달을 위해 meta를 사용함.
            yield scrapy.Request(url="https://corners.gmarket.co.kr" + category_link, callback=self.parse_detail,
                                 meta={'main_category_name': main_category_names[index],
                                       'sub_category_name': "ALL"})

        # 2) 서브 카테고리 크롤링
        # 중복된 url은 크롤링을 할 때, 넘어가는 경우가 있다.
        # setting.py에 DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter' 를 추가 입력한다.
        for index, category_link in enumerate(main_category_links):
            yield scrapy.Request(url="https://corners.gmarket.co.kr" + category_link, callback=self.parse_sub,
                                 meta={'main_category_name': main_category_names[index]})

    def parse_sub(self, response):
        print("-- parse_sub 함수 --")
        sub_category_links = response.css('div.navi.group > ul > li > a::attr(href)').getall()
        sub_category_names = response.css('div.navi.group > ul > li > a::text').getall()

        for index, sub_category_link in enumerate(sub_category_links):
            yield scrapy.Request(url="https://corners.gmarket.co.kr" + sub_category_link, callback=self.parse_detail,
                                 meta={'main_category_name': response.meta["main_category_name"],
                                       'sub_category_name': sub_category_names[index]})

    def parse_detail(self, response):
        print("-- parse_detail 함수 --", response.meta['main_category_name'], response.meta['sub_category_name'])
        # print("-- parse_detail 함수 --")

        main_items = response.css('div.best-list')
        # 페이지 소스보기로 best-list를 검색하면 3개가 나오는데, 원하는 값은 2번째에 존재함.
        for index, item in enumerate(main_items[1].css("li")):
            model = CategoryItem()

            ranking = index + 1
            title = item.css("a.itemname::text").get()
            ori_price = item.css("div.o-price span span::text").get()
            dis_price = item.css("div.s-price strong span span::text").get()
            discount_percent = item.css("div.s-price em::text").get()

            if dis_price is not None:
                dis_price = dis_price.replace(",", "").replace("원", "")

            if ori_price is None:
                ori_price = dis_price
            else:
                ori_price = ori_price.replace(",", "").replace("원", "")

            if discount_percent is None:
                discount_percent = "0"
            else:
                discount_percent = discount_percent.replace("%", "")

            model["main_category_name"] = response.meta["main_category_name"]
            model["sub_category_name"] = response.meta["sub_category_name"]
            model["ranking"] = ranking
            model["ori_price"] = ori_price
            model["dis_price"] = dis_price
            model["discount_percent"] = discount_percent
            model["title"] = title
            yield model

            # print("ranking : ", ranking, "\ntitle : ", title, "\nori_price : ", ori_price, "\ndis_price : ", dis_price,
            #       "\ndiscount_percent : ", discount_percent)
            #
            # print("\n\n")
