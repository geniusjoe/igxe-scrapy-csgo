import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_splash import SplashRequest
from . import items as items


#   terminal command:
#   docker run -p 8050:8050 scrapinghub/splash
#   scrapy crawl csgo_ig


class IgSpider(scrapy.Spider):
    name = "csgo_ig"

    base_url = 'https://www.igxe.cn'

    start_urls = ['https://www.igxe.cn/csgo/730']

    rules = (Rule(LinkExtractor(allow=('cur_page=3',), allow_domains=('www.igxe.cn'),
                                deny=('cur_page=1', 'cur_page=2', 'cur_page=4'))))

    lua_next_page = '''
    function main(splash)
      assert(splash:go(splash.args.url))
      assert(splash:wait(5))
      local old_html=splash:html()
      local getElementByXpath= splash:jsfunc([[
              function getElementByXpath(path) {
                  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                }
          ]])
        local element_click=splash:jsfunc([[
            function(element){
                element.click()
            }
        ]])
      local next_page_button=getElementByXpath(splash.args.trigger)
      element_click(next_page_button)
        splash:wait(5)

      return {
        html = old_html,
        url=splash:url(),
        }
    end
'''

    page_has_visited = []

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='execute',
                                args={
                                    'lua_source': self.lua_next_page,
                                    'trigger': '//*[@id="page-content"]/a[last()]',
                                }
                                )

    def parse(self, response):
        current_page_all_items = response.xpath(
            '//*[@id="center"]/div/div[3]/div/div[2]//a/@href').extract()
        for item in current_page_all_items:
            url = '{base_url}{item}?cur_page=3'.format(
                base_url=self.base_url, item=item)
            yield SplashRequest(url, self.weapon_parse, args={'wait': 5})
        current_page = response.xpath("//*[@id='page-content']//span[@class='active']//text()")
        if current_page != 462 and current_page != 461:
            next_page = response.xpath(
                "//*[@id='page-content']/a[last()]/@href")
            if next_page is not None:
                yield SplashRequest(response.data['url'], self.parse, endpoint='execute',
                                    args={
                                        'lua_source': self.lua_next_page,
                                        'trigger': '//*[@id="page-content"]/a[last()]',
                                    }
                                    )
        else:
            pass

    def weapon_parse(self, response):
        weapons = response.xpath(
            '//*[@id="id-box4-vue"]/div/div[2]/div[1]/div[2]/div[2]/div[3]/table/tbody//tr')
        for weapon in weapons:
            l = ItemLoader(item=items.weapon_ig_message(), response=response)
            name = weapon.xpath('td[2]/text()').extract()
            selling_price = weapon.xpath('td[4]/span/text()').extract()
            selling_date = weapon.xpath('td[3]/text()').extract()
            l.add_value('name', name)
            l.add_value('selling_price', selling_price)
            l.add_value('selling_date', selling_date)
            yield l.load_item()
