import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = [
        "https://bluelimelearning.github.io/my-fav-quotes/"
    ]

    def parse(self, response):
        for quote in response.css("div.quotes"):
            yield{
                'quote': quote.css('p.aquote::text').extract(),  # gets all the text
                'author': quote.css('p.author::text').extract_first(),  # gets only the first line
            }
