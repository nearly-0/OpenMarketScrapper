import scrapy

class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    pass

#
# class CommunitySpider(scrapy.Spider):
#     name = "communityCrawler"
#
#     #start_urls = {"https://www.clien.net/service/board/park?&od=T31&po=1"}
#
#     def start_requests(self):
#         yield scrapy.Request("https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100", self.parse_clien)
#         # for i in range(1, 2, 1):
#         #     yield scrapy.Request("https://www.clien.net/service/board/park?&od=T31&po=%d" %i, self.parce_clien)
#
#     def parse_clien(self, response):
#         print("Parsinggggggggg")
#         print(response.xpath(""))
#
#         for sel in response.xpath('/tbody/td[@class="aside"]/div[@class="aside"]/div[@class="section section_wide"]/div[@id="right.ranking_contents"]/ul[@class="section_list_ranking"]'):
#             print('==========================================================================\n')
#             print(sel)
#             print('==========================================================================\n')
#
#             item = DemoItem()
#
#             item['source'] = '클리앙'
#             item['category'] = 'free'
#
#             print('==========================================================================\n')
#             print(sel.xpath('/li/a/text()').extract() + "\n")
#             print(sel.xpath('/li/a/title/text()').extract() + "\n")
#             print('==========================================================================\n')
#
#             item['title'] = sel.xpath('/li/a/title/text()').extract()
#
#             print('==========================================================================')
#             print(item['title'])
#             print(item['source'])
#             print(item['title'])
#
#             yield item
#
#            # / div[2] / h3 / a
#             # question-summary-53988005 > div.summary > h3 > a
#            # // *[ @ id = "question-summary-53988005"] / div[2] / h3 / a
#            # // *[ @ id = "question-summary-54043472"]
#
#

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
                'test': quote.css('span a::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

class MovieSpider(scrapy.Spider):
    name = "movies"
    start_urls = [
        'https://www.imdb.com/list/ls021348496',
    ]

    def parse(self, response):
        for movie in response.css('div.lister-item.mode-detail'):
            item = DemoItem()

            # yield {
            #     'text' : quote.css('h3.lister-item-header a::text').extract_first()
            # }
            item['title'] = movie.css('h3.lister-item-header a::text').extract_first()

            print(item['title'])
            print("=================================================================================================================================\n")

class StackOverFlow(scrapy.Spider):
    name = "stacks"
    # start_urls = [
    #     #'https://stackoverflow.com/questions/tagged/c%2b%2b',
    #     'https://stackoverflow.com/questions/tagged/c%2b%2b?sort=newest&page=1',
    # ]

    def start_requests(self):
        for i in range(1, 10):
            yield scrapy.Request("https://stackoverflow.com/questions/tagged/c%2b%2b?sort=newest&page=" + 'i' + "&pagesize=1" , self.parse_stack)

    def parse_stack(self, response):
        for question in response.css('div.flush-left div.question-summary'):
            item = DemoItem()

            item['title'] = question.css('div.summary h3 a::text').extract_first()
            #print(item['title'])
            # yield {
            #     'text' : question.css('div.summary h3 a::text').extract_first()
            # }
            print("=======================================================================================================================================================================\n")
            yield item

