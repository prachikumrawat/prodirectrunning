import sys

from scrapy import pipelines

sys.path.append('../')
import pymongo
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import HtmlXPathSelector
from items import ProdirectItem
from utilities.restrictions import Restrictions
from utilities.start_url import Start_URL
from utilities.spider_settings import choose_settings, spider_settings
from utilities.price_converstion import PriceConverstion
from utilities.cleanup_class import CleanUp_class
# from pipelines import ProdirectPipeline
from utilities.db import ProdirectPipeline


class ReplenishmentSpider(CrawlSpider):
    name = 'pro_direct'
    allowed_domains = ['prodirectrunning.com']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        category_name = crawler.settings['category_name']
        spider = super(CrawlSpider, cls(category_name=category_name)).from_crawler(crawler, category_name=category_name)
        spider._follow_links = 'True'
        return spider

    def __init__(self, category_name, **kwargs):
        category_name = category_name
        print category_name
        start_url = Start_URL()
        self.start_urls = start_url.get_start_urls(category_name)
        self.cleanUp = CleanUp_class(category_name)
        sku_suffix = self.cleanUp.sku_suffix(category_name)
        self.restriction = Restrictions(sku_suffix)
        self.price_converstion = PriceConverstion(category_name)
        self.mongoDB = ProdirectPipeline(category_name)
        print self.mongoDB
        self.matser_asins = self.mongoDB.get_inventory(
            sku_suffix=sku_suffix,
            script_type="replenishment",
            category_name=category_name
        )
        super(ReplenishmentSpider, self).__init__()

    def parse_item(self, response):
        print response
        item = ProdirectItem()
        hxs = HtmlXPathSelector(response)
        item['product_name'] = hxs.select('//*[@id="define-profile"]/h1/text()').extract()
        item['description'] = hxs.select('//*[@id="content"]/div/div[4]/div[1]/div/div[2]/div[1]/text()').extract()
        item['price'] = hxs.select('//*[@id="define-profile"]/p[3]/text()').extract_first()
        item['image'] = hxs.xpath('//img/@src').extract_first(),
        item['product_url'] = response.url

        return item


def start_spider():
    start_urls = Start_URL()
    category_name = start_urls.user_input()

    settings = spider_settings
    settings['category_name'] = category_name
    settings.update(choose_settings())

    process = CrawlerProcess(settings)
    process.crawl(ReplenishmentSpider)
    process.start()


if __name__ == '__main__':
    start_spider()
















 # start_urls_list = []
    # start_url_file_path = os.path.realpath('../utilities/bin/start_url/prodirect/start_URL.csv')
    # start_urls_category_list = []
    # with open(start_url_file_path, 'r') as start_url_file:
    #     for row in csv.DictReader(start_url_file):
    #         if row['Category'] not in start_urls_category_list:
    #             start_urls_category_list.append(row['Category'])
    #             row['URL'] = row['URL'].replace('+AC0', '')
    #             start_urls_list.append(row['URL'])
    #
    # sorted_list = sorted(start_urls_category_list)
    # for index, category in enumerate(sorted_list, 1):
    #     print '{0}. {1}'.format(index, category)
    #
    # script_choice = int(raw_input("Choose Category:\n"))
    # if script_choice == 1:
    #     start_urls_list = start_urls_list[1:3]
    # elif script_choice == 2:
    #     start_urls_list == start_urls_list[3:]
    # print start_urls_list
    # start_urls = start_urls_list
    # rules = [Rule(LinkExtractor(allow='/products/'), callback='parse_item', follow=False)]
