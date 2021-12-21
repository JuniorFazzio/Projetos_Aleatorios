import csv

class PLanilhaCSV:
    '''
    Classe criada para realizar o armazenamento do scrapping realizado
    dentro de um CSV
    '''

    def __init__(self, lista_nomes, lista_secao, lista_preco, lista_avalicao): #iniciando classe passando as listas de dados
        self.lista_nomes = lista_nomes
        self.lista_secao = lista_secao
        self.lista_preco = lista_preco
        self.lista_avalicao = lista_avalicao

    def criar_armazenar_csv(self): #aqui vamos criar o arquivo e armazenar os dados das listas
        with open('scrapping.csv', 'a', newline='') as csvfile:

            nome_colunas = ['Nome', 'Secao', 'Preco', 'Avaliacao'] #criando nome das colunas
            arquivo = csv.DictWriter(csvfile, fieldnames= nome_colunas) #criando para armazenar!

            #Criando o cabeçalho!
            arquivo.writeheader()

            #Iterando
            if len(self.lista_nomes) == len(self.lista_secao) == len(self.lista_preco) == len(self.lista_avalicao): #proteção para funcionar!
                print('Gravando dados!')
                for i in range(len(self.lista_nomes)):
                    arquivo.writerow({'Nome': f'{self.lista_nomes[i]}',
                                      'Secao': f'{self.lista_secao[i]}',
                                      'Preco': f'{self.lista_preco[i]}',
                                      'Avaliacao': f'{self.lista_avalicao[i]}'})
            else: #excessão
                print('Há algum problema de tamanho das listas!\nVerifique!')
                                    
