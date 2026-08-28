import scrapy

from news_scraper.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = NewsItem()

            item["title"] = quote.css("span.text::text").get()
            item["url"] = response.url
            item["source"] = "Quotes to Scrape"
            item["author"] = quote.css("small.author::text").get()
            item["published_at"] = None
            item["category"] = None
            item["content"] = quote.css("span.text::text").get()
            item["image"] = None
            item["scraped_at"] = None

            yield item
