import sys
from planilha import Planilhas

if __name__ == "__main__":
    try:
        arquivo_entrada = str(sys.argv[1])
        arquivo_saida = str(sys.argv[2])
        Planilhas(arquivo_entrada, arquivo_saida)
    except (IndexError, ValueError):
        print("Uso: python main.py arquivo_entrada.xlsx relatorio_gerado.csv")
        sys.exit(1)
