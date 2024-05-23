import pandas as pd
import states
import re

class Planilhas():
    def __init__(self, arquivo_entrada, arquivo_saida):
        self.panda = pd
        self.xlsx = self.panda.read_excel(arquivo_entrada, engine='openpyxl')
        self.csv = arquivo_saida
        self.states = states.states
        self.create_csv()
    
    def create_csv(self):

        self.converte_cnpj() # chama funcao de conversao do cnpj, tirando os caracteres especiais
        self.converte_uf() # chama funcao de conversao da UF, da sigla para o nome completo 
        self.converte_data() # ainda nao implementado
        self.converte_numero() # chama funcao de conversao do valor do pagamento, formantando as casas decimais com virgula

        self.xlsx.sort_values(by='Forma Lancamento').to_csv(self.csv, index=False,sep=";") # criando o csv
        print(self.xlsx)
        
    def converte_cnpj(self):
        
        cont = 0

        for cnpj in self.xlsx["Numero Incricao Empresa"]:
            new_cnpj = re.sub("[^0-9]","", str(cnpj))
            print(f"Convertendo CNPJ, de {cnpj} para {new_cnpj}")
            self.xlsx.at[cont, "Numero Incricao Empresa"] = new_cnpj
            cont += 1 
            if cont > self.xlsx.shape[0]:
                break
    
    def converte_uf(self):

        cont = 0

        for uf in self.xlsx["Estado"]:
            self.xlsx.at[cont, "Estado"] = self.states[uf]
            print(f"Convertendo Estado, de {uf} para {self.states[uf]}")
            cont += 1 
            if cont > self.xlsx.shape[0]:
                break
    
    def converte_numero(self):

        cont = 0

        for num in self.xlsx["Valor Pagamento"]:
            new_num = format(int(re.sub("[^0-9]","", str(num))), ",")
            print(f"Convertendo Valor do Pagamento, de {num} para {new_num}")
            self.xlsx.at[cont, "Valor Pagamento"] = new_num
            cont += 1 
            if cont > self.xlsx.shape[0]:
                break

    def converte_data(self):
        pass