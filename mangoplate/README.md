# Mangoplate Scrapy Spiders

This repository contains two Scrapy spiders for web scraping restaurant information from the Mangoplate website. The spiders are built using Scrapy, a powerful and flexible web scraping framework in Python. The scraped data is then saved to a MongoDB database for easy querying and analysis.

## Prerequisites

Before running the spiders, you need to ensure that you have the following dependencies installed:

- Python 3.x
- Scrapy
- pymongo
- MongoDB

You can install Scrapy and pymongo using pip:

```bash
pip install scrapy pymongo
```

## Mangoplate_lv Spider

The `mangoplate_lv` Scrapy spider is designed to scrape restaurant information from the Mangoplate website for the keyword "Hongdae." It scrapes multiple pages of search results and saves the data to a MongoDB collection named `hongdae_lv`.

### Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/mangoplate_spiders.git
cd mangoplate_spiders
```

2. Start your MongoDB server and make sure it's running on `localhost:27017`.

3. Run the `mangoplate_lv` spider:

```bash
scrapy crawl mangoplate_lv
```

The spider will start scraping restaurant information for the keyword "Hongdae" from the Mangoplate website. The data will be saved to the `hongdae_lv` MongoDB collection.

### Output

The `mangoplate_lv` spider will extract the following restaurant information:

- Name
- Branch
- Review score
- Review count
- Cuisine
- View count
- URL (Mangoplate page URL)

The data will be saved in MongoDB as documents in the `hongdae_lv` collection.

### Pagination

The `mangoplate_lv` spider is set to scrape multiple pages of search results. It starts with page 1 and continues until page 10. You can change the number of pages to scrape by modifying the `page_number` attribute in the spider.

## Mangoplate_pv Spider

The `mangoplate_pv` Scrapy spider is designed to scrape detailed restaurant information from specific URLs on the Mangoplate website. It takes a list of restaurant URLs from the `hongdae_lv` MongoDB collection as input and saves the filtered data to a new MongoDB collection named `hongdae_pv`.

### Usage

1. Clone this repository to your local machine (if not done already):

```bash
git clone https://github.com/yourusername/mangoplate_spiders.git
cd mangoplate_spiders
```

2. Start your MongoDB server and make sure it's running on `localhost:27017`.

3. Run the `mangoplate_pv` spider:

```bash
scrapy crawl mangoplate_pv
```

The spider will start scraping detailed restaurant information from the specified URLs on the Mangoplate website. The filtered data will be saved to the `hongdae_pv` MongoDB collection.

### Output

The `mangoplate_pv` spider will extract the following detailed restaurant information:

- Address
- Phone Number
- Cuisine
- Price Range
- Parking Availability
- Business Hours
- Break Time
- Last Order
- Day Off
- Website URL
- Image URL

The data will be saved in MongoDB as documents in the `hongdae_pv` collection.

### Filtering

The `mangoplate_pv` spider filters out specific strings (`skip_string`) and non-English characters from the extracted data to ensure accurate and relevant information.