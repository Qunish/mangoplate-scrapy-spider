import scrapy
from ..items import MangoplateItem_lv
import pymongo

class MangoplateLvSpider(scrapy.Spider):
    name = "mangoplate_lv"
    page_number = 2
    start_urls = [
        "https://www.mangoplate.com/en/search/Hongdae?keyword=Hongdae&page=1"
    ]

    def __init__(self):
        self.conn = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = self.conn["mangoplate_data_db"]
        self.collection = db["hongdae_lv"]

    def parse(self, response):
        items = MangoplateItem_lv()
        all_cards = response.xpath("/html/body/main/article/div[2]/div/div/section/div[3]/ul/li/div/figure")

        for card in all_cards:
            try:
                name = card.css(".restaurant-item .title::text").get().replace("\n", "").strip()
            except Exception as e:
                name = ""
            try:
                branch = card.css(".branch::text").get().replace("\n", "").strip()
            except Exception as e:
                branch = ""
            try:
                review = card.css(".search_point::text").get().replace("\n", "").strip()
            except Exception as e:
                review = ""
            try:    
                review_count = card.css(".review_count::text").get().replace("\n", "").strip()
            except Exception as e:
                review_count = ""
            try:
                cuisine = card.css(".etc span::text").get().replace("\n", "").strip()
            except Exception as e:
                cuisine = ""
            try:
                view_count = card.css(".view_count::text").get().replace("\n", "").strip()
            except Exception as e:
                view_count = ""
            base_url = card.css(".info a::attr(href)").get()
            url = ("https://www.mangoplate.com")+base_url

            items["name"] = name
            items["branch"] = branch
            items["review"] = review
            items["review_count"] = review_count
            items["cuisine"] = cuisine
            items["view_count"] = view_count
            items["url"] = url

            self.collection.insert_one(dict(items))

            yield items
        next_page = "https://www.mangoplate.com/en/search/Hongdae?keyword=Hongdae&page=" + str(MangoplateLvSpider.page_number)
        if MangoplateLvSpider.page_number < 11:
            MangoplateLvSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
