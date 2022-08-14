import scrapy
from..items import MangoItem

class MangoItemSpider(scrapy.Spider):
    name = 'mango'
    start_urls = ['https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99']

    def parse(self, response):
        items = MangoItem()

        product_name = response.css('.product_name::text').extract()
        product_color = response.css('.color-image--no-stock , #99 #08').css('::text').extract()
        product_price = response.css('.product-sale--discount').css('::text').extract()
        product_size = response.css('.span.size-unavailable').css('::text').extract()

        items['product_name'] = product_name
        items['product_color'] = product_color
        items['product_price'] = product_price
        items['product_size'] = product_size

        yield items
