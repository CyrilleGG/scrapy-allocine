import scrapy

class SeriesSpider(scrapy.Spider):
  name = "series"

  start_urls = ['http://www.allocine.fr/series/nouvelles/']

  def parse(self, response):
    self.logger.info('hello first!')
    series = response.css("li.mdl")
    for serie in series:
      yield {
        'title': serie.css(".meta-title-link::text").get(),
        'genre': serie.css("div.meta-body-info span:not(.spacer)::text").getall(),
        'direction': serie.css("div.meta-body-direction span::text").getall(),
        'summary': serie.css(".synopsis .content-txt::text").get(),
      }
    pass