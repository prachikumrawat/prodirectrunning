import sys
sys.path.append('../')
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule

from utilities.start_url import Start_URL
from utilities.spider_settings import spider_settings,choose_settings


class UpdateSpider(CrawlSpider):
    name = 'prodirect'
    #allowed_domains = ['prodirectrunning.com']
    ## start_urls = ['http://www.prodirectrunning.com/lists/mens-running-shoes.aspx']

   # rules = [
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        #Rule(LinkExtractor(allow='/products/', ), callback='parse_item')
    #]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        category_name = crawler.settings['category_name']
        spider = super(CrawlSpider, cls(category_name=category_name)).from_crawler(crawler,category_name=category_name)
        spider._follow_links = 'True'
        return spider

    def __init__(self,*args,**kwargs):

        category_name = kwargs['category_name']
        print category_name
        start_url = Start_URL()
        self.start_urls = start_url.get_start_urls(category_name)


    def parse_item(self, response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        pass


def start_spider():
    start_urls = Start_URL()
    category_name = start_urls.user_input()

    settings = spider_settings
    settings['category_name'] = category_name
    settings.update(choose_settings())

    process = CrawlerProcess(settings)
    process.crawl(UpdateSpider)
    process.start()

if __name__=='__main__':
    start_spider()

