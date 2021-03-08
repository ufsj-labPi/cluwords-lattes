import scrapy

class LattesSpider(scrapy.Spider):
    name = "curriculos"

    def start_requests(self):
        urls = []

        for i in range(0,343415,10):
            urls.append('http://buscatextual.cnpq.br/buscatextual/busca.do?'+\
                        'metodo=forwardPaginaResultados&registros='+str(i)+\
                        ';10&query=%28+%2Bidx_formacao_academica%3Adoutorado+++++++++++++++'+\
                        '%2Bidx_particao%3A1+%2Bidx_nacionalidade%3Ae%29+or+%28+'+\
                        '%2Bidx_formacao_academica%3Adoutorado+++++++++++++++'+\
                        '%2Bidx_particao%3A1+%2Bidx_nacionalidade%3Ab+%5E500+'+\
                        '%29&analise=cv&tipoOrdenacao=null&paginaOrigem=index.do&'+\
                        'mostrarScore=false&mostrarBandeira=true&modoIndAdhoc=null')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for resultado in response.css('div.resultado li'):
            
            NAME_SELECTOR = 'a ::text'
            ID10_SELECTOR = 'a::attr(href)'
            INFO_SELECTOR = 'li ::text'
            
            json_saida = {
                'nome': resultado.css(NAME_SELECTOR).get(),
                'ID10': (resultado.css(ID10_SELECTOR).re(r"\('\w+"))[0][2:],
                'info': (resultado.css(INFO_SELECTOR).getall())[2],
            }

            with open('lattes_spider.csv','a') as f:
                f.write('"'+json_saida['nome']+'";"'+json_saida['ID10']+'";"'+json_saida['info']+'"\n')

            yield json_saida