import scrapy


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()
    author = scrapy.Field()
    published_at = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()
    image = scrapy.Field()
    scraped_at = scrapy.Field()
