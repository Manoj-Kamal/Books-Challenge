import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    base_url = 'http://books.toscrape.com/'

    def parse(self, response):
        books = response.xpath('.//article[@class="product_pod"]')
        for book in books:
           
           # Saving Scraped content to respective variables

            full_url = book.xpath('.//h3/a/@href').extract_first()
                                    
            title = book.xpath('.//h3/a/@title').extract_first()

            price = book.xpath('.//div/p[@class="price_color"]/text()').extract_first()

            image_src = book.xpath('.//div[@class="image_container"]/a/img/@src').extract_first()

            full_image_src = self.base_url + image_src.replace('../', '')
          
          # Getting the Absolute path

            if 'catalogue/' not in full_url:
                full_url = 'catalogue/' + full_url
        
            full_url = self.base_url + full_url

            yield {
                'Title': title,
                'Price': price,
                'Image URL': full_image_src,
                'Book URL': full_url,
            }
        # Fetching Next Page URL and parsing to the callback function
        
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)