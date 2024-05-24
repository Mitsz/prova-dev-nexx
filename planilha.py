import pandas
import states
import re
import locale

class Planilhas():
    def __init__(self, arquivo_entrada, arquivo_saida):
        self.panda = pandas
        self.xlsx = self.panda.read_excel(arquivo_entrada, engine='openpyxl')
        self.csv = arquivo_saida
        self.states = states.states
        locale.setlocale(locale.LC_ALL, 'pt_BR')
        self.create_csv()
    
    def create_csv(self):
        '''Gera o log do processamento dos dados, e cria o CSV com base no XLSX de entrada'''

        print("XLSX lido com sucesso: ")
        print(self.xlsx)

        print("Retirando formatacao do CNPJ: ")
        self.converte_cnpj() # chama funcao de conversao do cnpj, tirando os caracteres especiais
        print(self.xlsx["Numero Incricao Empresa"].to_string(index=False))

        print("Convertendo coluna Estado: ")
        self.converte_uf() # chama funcao de conversao da UF, da sigla para o nome completo 
        print(self.xlsx["Estado"].to_string(index=False))

        print("Convertendo coluna Valor Pagamento: ")
        self.converte_numero() # chama funcao de conversao do valor do pagamento, formantando as casas decimais com virgula
        print(self.xlsx["Valor Pagamento"].to_string(index=False)) 

        print("Convertendo coluna Data Pagamento: ")
        self.converte_data()
        print(self.xlsx["Data Pagamento"].to_string(index=False))

        print(f"Ordenando linhas pela coluna Forma Lancamento, e gerando CSV final com nome {self.csv}: ")

        self.xlsx.sort_values(by='Forma Lancamento').to_csv(self.csv, index=False,sep=";") # criando o csv e ordenando pela forma de lancamento
        print(self.xlsx.sort_values(by='Forma Lancamento'))

    def converte_cnpj(self):
        
        cont = 0

        for cnpj in self.xlsx["Numero Incricao Empresa"]:
            new_cnpj = re.sub("[^0-9]","", str(cnpj))
            self.xlsx.at[cont, "Numero Incricao Empresa"] = new_cnpj
            cont += 1 
            if cont > self.xlsx.shape[0]:
                break
    
    def converte_uf(self):

        cont = 0
        for uf in self.xlsx["Estado"]:
            self.xlsx.at[cont, "Estado"] = self.states[uf]
            cont += 1 
            if cont > self.xlsx.shape[0]:
                break
    
    def converte_numero(self):

        cont = 0

        for num in self.xlsx["Valor Pagamento"]:
            new_num = "{:,.2f}".format(int(re.sub("[^0-9]","", str(num)))/100)
            self.xlsx.at[cont, "Valor Pagamento"] = re.sub("[.]",",", str(new_num))
            cont += 1 
            if cont > self.xlsx.shape[0]:
                break

    def converte_data(self):

        self.xlsx["Data Pagamento"] = self.panda.to_datetime(self.xlsx["Data Pagamento"].dt.strftime('%Y-%d-%m'))
        self.xlsx["Data Pagamento"] = self.xlsx["Data Pagamento"].dt.strftime("%d/%B/%Y")
