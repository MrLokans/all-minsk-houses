from scrapy.item import Item, Field


class Street(Item):
    url = Field()
    name = Field()
    houses = Field()
