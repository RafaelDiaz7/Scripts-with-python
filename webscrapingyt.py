from  scrapy.item import Field
from  scrapy.item import Item
from  scrapy.spiders import Spider
from  scrapy.selector import selector
from  scrapy.contrib.loader import ItemLoader

#Web Scraping script for get neurocience youtube videos data 

class VideoTitle(Item):
    video = Field()
    id = Field()

class YoutubeSpider(Spider):
    name = 'SpiderForYoutube'
    start_urls = ['https://www.youtube.com/results?search_query=neurociencia']
    def parse(self, response):
        sel = Selector(response)
        video_titles = sel.xpath('//div[@id="contents"]/div')

        #Iterate over all the titles
        for i, elem in enumerate(video_titles):
            item = ItemLoader(VideoTitle(), elem)