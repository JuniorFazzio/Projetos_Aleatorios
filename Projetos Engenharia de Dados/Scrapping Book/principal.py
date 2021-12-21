import scrapping
 
#Iniciando nosso programa

raspagem = scrapping.Scrapping('http://books.toscrape.com/catalogue/page-1.html')
raspagem.scrapping()
raspagem.Armazenar()
