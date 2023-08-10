import scrapy
import os

class PrecoCelutaresSpider(scrapy.Spider):
    name = 'botCelularPrice'
    urls = ['https://telefonesimportados.netlify.app']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self,response):
        for elemento in response.xpath("//div[@class='single-shop-product']"):
            yield {
                'Marca': elemento.xpath(".//h2//text()").get(),
                'Preço': elemento.xpath(".//div[@class='product-carousel-price']//ins//text()").get()
            }

        proxima_pagina = response.xpath("//div[@class='product-pagination text-center']//li//a[@aria-label='Next']/@href").get()
        if proxima_pagina:
            link_completo = response.urljoin(proxima_pagina)
            yield scrapy.Request(url=link_completo, callback=self.parse)
        else:
            print(f'Preços varridos com sucesso!{os.linesep}Enviando o Relatório para o Email')
            