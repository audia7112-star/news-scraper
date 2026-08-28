import scrapy

from news_scraper.items import NewsItem


class ReutersSpider(scrapy.Spider):
    name = "reuters"
    allowed_domains = ["reuters.com"]

    custom_settings = {
        "ROBOTSTXT_OBEY": True,
        "DOWNLOAD_DELAY": 2,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
    }

    # Gunakan URL artikel Reuters yang memang ingin Anda uji.
    start_urls = [
        "https://www.reuters.com/world/india/india-wanted-red-flags-chip-packets-soda-big-food-fought-back-2026-08-25/"
    ]

    def parse(self, response):
        title = response.css("h1::text").get()

        authors = response.css(
            'a[href*="/authors/"]::text'
        ).getall()

        published_at = response.css(
            "time::attr(datetime)"
        ).get()

        paragraphs = response.css(
            "div.article-body__content__17Yit p::text"
        ).getall()

        if not paragraphs:
            paragraphs = response.css(
                "article p::text"
            ).getall()

        content = "\n\n".join(
            paragraph.strip()
            for paragraph in paragraphs
            if paragraph.strip()
        )

        image = response.css(
            'meta[property="og:image"]::attr(content)'
        ).get()

        yield NewsItem(
            title=title.strip() if title else None,
            url=response.url,
            source="Reuters",
            author=", ".join(
                author.strip()
                for author in authors
                if author.strip()
            ) or None,
            published_at=published_at,
            category=None,
            content=content or None,
            image=image,
            scraped_at=None,
        )
