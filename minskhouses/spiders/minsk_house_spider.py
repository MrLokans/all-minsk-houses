# coding: utf8

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from scrapy.selector import Selector

from scrapy.item import Item, Field


class Street(Item):
    url = Field()
    name = Field()
    houses = Field()


BASE_URL = "http://ato.by"
PAGES = list(range(1, 8)) + list(range(9, 12)) + list(range(13, 29))
PAGES.extend(list(range(30, 33)))

STREET_URL = BASE_URL + '/streets/letter'


def correct_encoding(s):
    if hasattr(s, "encode"):
        return s.encode('utf-8').decode('utf-8')


class BookSpider(CrawlSpider):
    name = "minskhousesspider"
    allowed_domains = ["ato.by"]
    start_urls = ["/".join([STREET_URL, str(i)]) for i in PAGES]

    rules = [
        Rule(LinkExtractor(allow=(r'/street/\d+')),
             callback='parse_topic_page',
             follow=True)]

    def parse_topic_page(self, response):
        street = Street()

        street["url"] = response.url

        street_name_selector = "//div[@class='intro']/h3/text()"
        house_selector = "//a[re:test(@href, '/address/\d+-\d+')]/text()"

        street_name = response.xpath(street_name_selector).extract_first()
        street_name = street_name.encode('utf-8').decode('utf-8')
        street["name"] = street_name
        houses = response.xpath(house_selector).extract()
        houses = list(filter(lambda x: x.strip() != u"карта", houses))
        street["houses"] = houses

        yield street
