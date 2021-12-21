from selenium import webdriver
from time import sleep
import armazenando_csv

class Scrapping:

    '''
    Classe criada para realizar o scrapping de dados da internet
    Mais especificamente do site http://books.toscrape.com/catalogue/page-1.html
    '''

    def __init__(self, site): #inicialização da classe
        self.driver = webdriver.Edge(r'C:\\Users\\ademi\\OneDrive\\Documentos\\Estudos Python\\Projetos Aleatórios\\Projetos Engenharia de Dados\\Scrapping Book\\msedgedriver.exe')
        self.driver.get(site)
        print('Inicizaliando Site!')
        sleep(2)

    def scrapping(self): #aqui ele realiza o scrapping

        #criando variaveis para armazenar dados
        self.lista_nomes = []
        self.lista_secao = []
        self.lista_preco = []
        self.lista_avalicao = []

        #criando o loop
        while True:

            iter = 1 #definindo inicio de elementos

            while True: #pegando informações

                link = self.driver.find_elements_by_xpath(f'//ol[@class="row"]//li [{iter}]//a') #acessa link dos livros
                tamanho = len(link)

                if tamanho > 0:
                    link[0].click()
                    sleep(2)

                    #pega os dados
                    self.lista_nomes.append(self.driver.find_elements_by_xpath('//div[@class="col-sm-6 product_main"]//h1')[0].text)
                    self.lista_secao.append(self.driver.find_elements_by_xpath('//ul[@class="breadcrumb"]//li [3]')[0].text)
                    self.lista_preco.append(self.driver.find_elements_by_xpath('//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')[0].text)
                    self.lista_avalicao.append(self.driver.find_elements_by_xpath('//div[@class="col-sm-6 product_main"]//p [3]')[0].get_attribute('class'))


                    self.driver.execute_script("window.history.go(-1)") #voltando na página anterior
                    print(f'Livros coletados nessa página: {iter}')
                    iter += 1
                
                else: #saindo caso não tenha mais livros para varrer
                    print('Terminamos os livros dessa página!\n')
                    break
            
            next = self.driver.find_elements_by_xpath('//li[@class="next"]//a') #pegando botão de next

            if len(next) > 0: #vamos passar para próxima página
                print('Vamos passar para a próxima página!\n')
                next[0].click()
            
            else: #saindo das iterações
                print('Terminamos de coletar todos os livros!')
                break

    def Armazenar(self): #aqui vamos chamar nossa biblioteca de armazenamento em csv
        armazenador = armazenando_csv.PLanilhaCSV(self.lista_nomes, self.lista_secao, self.lista_preco, self.lista_avalicao)
        armazenador.criar_armazenar_csv()

        