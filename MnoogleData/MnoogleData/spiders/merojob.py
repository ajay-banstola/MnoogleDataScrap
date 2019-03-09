# -*- coding: utf-8 -*-
import scrapy


class MerojobSpider(scrapy.Spider):
	name = 'merojob'
	allowed_domains = ['merojob.com']
	start_urls = ['https://merojob.com/services/top-job/',
	'https://merojob.com/category/construction-engineering-architects/',
	'https://merojob.com/category/teaching-education/',
	'https://merojob.com/category/marketing-advertising-customer-service/',
	'https://merojob.com/category/accounting-finance/',
	'https://merojob.com/category/sales-public-relations/',
	'https://merojob.com/category/it-telecommunication/',
	'https://merojob.com/category/healthcare-pharma-biotech-medical-rd/',
	'https://merojob.com/category/ngo-ingo-social-work/',
	'https://merojob.com/category/general-mgmt-administration-operations/',
	'https://merojob.com/category/banking-insurance-financial-services/',
	'https://merojob.com/category/hospitality/',
	'https://merojob.com/category/journalism-editor-media/',
	'https://merojob.com/category/secretarial-front-office-data-entry/',
	'https://merojob.com/category/production-maintenance-quality/',
	'https://merojob.com/category/creative-graphics-designing/',
	'https://merojob.com/category/commercial-logistics-supply-chain/',
	'https://merojob.com/category/protective-security-services/',
	'https://merojob.com/category/human-resource-org-development/',
	'https://merojob.com/category/research-and-development/',
	'https://merojob.com/category/architecture-interior-designing/',
	]
	
	def parse(self, response):
		Company = response.xpath('//*[@class="no-uline"]/@title').extract()
		Product = response.xpath('//*[@class="text-primary h5"]/@title').extract()
		Address = response.xpath('//*[@itemprop="addressLocality"]/text()').extract()
		Deadline = response.xpath('//*[@itemprop="validThrough"]/@content').extract()
		
		for item in zip(Company,Product,Address,Deadline):
			scraped_info = {
				'Company':item[0],
				'Product':item[1],
				'Address':item[2],
				'Deadline':item[3],
			}
			yield scraped_info
		
		next_page_url = response.xpath('//li/a[@class="pagination-next page-link"]/@href').extract_first()
		next_page_url = response.urljoin(next_page_url)
		if next_page_url:
			yield scrapy.Request(url = next_page_url, callback = self.parse)