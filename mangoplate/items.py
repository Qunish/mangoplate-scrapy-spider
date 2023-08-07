# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MangoplateItem_lv(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    branch = scrapy.Field()
    review = scrapy.Field()
    review_count = scrapy.Field()
    cuisine = scrapy.Field()
    view_count = scrapy.Field()
    url = scrapy.Field()
    pass

class MangoplateItem_pv(scrapy.Item):
    favorite = scrapy.Field()
    address = scrapy.Field()
    price_range = scrapy.Field()
    parking = scrapy.Field()
    business_hours = scrapy.Field()
    break_time = scrapy.Field()
    last_order = scrapy.Field()
    website = scrapy.Field()
    image_url = scrapy.Field()
    phone_number = scrapy.Field()
    cuisine = scrapy.Field()
    day_off = scrapy.Field()
    
    pass