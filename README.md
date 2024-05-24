# Prova para o Desenvolvimento Nexxera
Este repositório tem como intuito o desenvolvimento de um programa que realize a leitura de um XLSX e o converta em um CSV. Além disso, algumas regras devem ser levadas em consideração. São elas:]

1 - A Coluna B "Numero Incricao Empresa" deve ser inserido no CSV sem formatação.

2 - A Coluna G "Estado" deve convertrer a sigla da UF para a literal.

3 - A Coluna J "Data Pagamento" deve converter o formato da data original (mm-dd-yy) para dd/Mes-por-extenso/YYYY.

4 - A Coluna K "Valor Pagamento" deve ser formatado com dois números decimais, e inserir um separador nas centenas. Deve ser separado por vírgula.

5 - As demais Colunas não devem ser alteradas.

6 - O CSV deve ser ordenado pela coluna "Forma Lancamento"

7 - O CSV deve ser separado por ponto-e-vírgula.

# Execução do programa:
python main.py arquivo_entrada.xlsx relatorio_gerado.csv

# Instalar Dependencias:
pip install -r requirements.txt
