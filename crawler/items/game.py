from scrapy import Item, Field


class GameItem(Item):
    
    title = Field()
    site_id = Field()
    original_price = Field()
    discount_price = Field()

# End Of File