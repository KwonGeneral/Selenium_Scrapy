# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestItem(scrapy.Item):
    # 여기에 항목에 대한 필드를 다음과 같이 정의하십시오:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()


class CategoryItem(scrapy.Item):
    main_category_name = scrapy.Field()
    sub_category_name = scrapy.Field()
    title = scrapy.Field()
    ranking = scrapy.Field()
    ori_price = scrapy.Field()
    dis_price = scrapy.Field()
    discount_percent = scrapy.Field()

