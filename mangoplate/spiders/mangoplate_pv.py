import scrapy
from ..items import MangoplateItem_pv
import pymongo

class MangoplatePvSpider(scrapy.Spider):
    name = "mangoplate_pv"

    def __init__(self):
        self.conn = pymongo.MongoClient(
            "localhost",
            27017
        )
        self.db = self.conn["mangoplate_data_db"]
        self.collection = self.db["hongdae_lv"]
        result = self.collection.find({})
        result = list(result)
        self.start_urls = [document['url'] for document in result]

        self.pv_collection = "hongdae_pv"  # New collection 'hongdae_pv'
        self.pvcollection = self.db[self.pv_collection]
        

    def parse(self, response):
        item = MangoplateItem_pv()

        details = response.css(".info")
        data_list = []
        for i in details.css("::text").extract():
            data_list.append(i.replace("\n", "").strip())

        skip_string = ['', 'Restaurant detailed information', 'Menu']

        result = [i for i in data_list if i not in skip_string and i.isascii()]

        fields = ['Address', 'Phone Number', 'Cuisine' 'Price Range', 'Parking', 'Business Hours', 'Break Time', 'Last Order', 'Day Off']

        # Create an empty dictionary to store key-value pairs
        info_dict = {}
        # Loop through the fields list and check if each item is in the result list
        for k in fields:
            if k in result and result.index(k) + 1 < len(result):
                # Get the index of the key in the result list
                key_index = result.index(k)
                # The next item in the result list will be the value
                value = result[key_index + 1]
                info_dict[k] = value

        # Assign the filtered data to the item dynamically
        for key, value in info_dict.items():
            item[key.lower().replace(" ", "_")] = value

        try:
            item['website'] = response.css(".under_line::attr(href)").get().replace("\n", "").strip()
        except Exception as e:
            item['website'] = ""
        try:
            item['image_url'] = response.css(".center-croping::attr(src)").get().replace("\n", "").strip()
        except Exception as e:
            item['image_url'] = ""

        # Save the item to MongoDB
        self.pvcollection.update_one(
            {'url': response.url},
            {'$set': dict(item)},
            upsert=True
        )
        print("After MongoDB Update:", item)
        yield item