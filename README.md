# Coding Assignment - 2.1
**Summary:**

This spider will scrape the first 750 items from books.toscrape.com website using item pipeline and exports the output to Dropbox using API Token for the following fields:

Book Title
Product Price
Image URL and 
Book URL


Please create a new scrapy project using the commands given below and overwrite the original files books.py, settings.py and pipelines.py from this project

```
scrapy startproject books_challenge
scrapy genspider books books.toscrape.com
```

To export the data into a JSON file, please execute the below command:

```
scrapy crawl books -o output.json
```

To stop the Spider after scraping n number of items I have implemented item pipeline with below condition. The scrapy will have to process the items which are already in the process of yielding when used without below pipeline and this causes it to yield 10-20 items extra.
We have to use the below pipeline to Drop the ITEMS right after the 750 items count has reached because the CLOSESPIDER_ITEMCOUNT will not immediately stop/close the spider as soon as the limit is reached. 

```
    def process_item(self, item, spider):
        if self.settings['CLOSESPIDER_ITEMCOUNT'] != 0 and self.itemCount >= self.settings['CLOSESPIDER_ITEMCOUNT']:
            raise DropItem(
                "ClOSESPIDER_ITEMCOUNT limit reached - " + str(self.settings['CLOSESPIDER_ITEMCOUNT']))
        else:
            self.itemCount += 1
            pass
        return item
```

To modify the item count, edit the CLOSESPIDER_ITEMCOUNT value in the settings.py file

```
CLOSESPIDER_ITEMCOUNT = 750 //current value
```

To Export the Scraped items to the Dropbox, you can use the plugin scrapy-feedexporter-dropbox.

Install the scrapy-feedexporter-dropbox plugin using the below command

For the demonstartion, I have used a throwaway dropbox account.

```
pip install git+https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox.git
```

For more details about the dropbox plugin, please refer the following URL : https://github.yuuza.net/scrapy-plugins/scrapy-feedexporter-dropbox

Happy Scraping!
