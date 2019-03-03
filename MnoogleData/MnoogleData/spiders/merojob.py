# -*- coding: utf-8 -*-
import scrapy


class MerojobSpider(scrapy.Spider):
	name = 'merojob'
	allowed_domains = ['merojob.com']
	start_urls = ['https://merojob.com/services/top-job/']
	
	def parse(self, response):
		Company = response.xpath('//*[@class="no-uline"]/@title').extract()
		product = response.xpath('//*[@class="col-lg-9 col-md-9 pl-0 pt-2"]//h3//a/text()').extract()
		address = response.xpath('//*[@class="text-muted"]/span/text()').extract()
		
		for item in zip(Company,product,address):
			scraped_info = {
				'Company':item[0],
				'product': item[1],
				'Address':item[2],

			}
			yield scraped_info
