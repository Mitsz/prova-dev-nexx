import sys
from planilha import Planilhas
import zipfile

if __name__ == "__main__":
    try:
        arquivo_entrada = str(sys.argv[1])
        arquivo_saida = str(sys.argv[2])
        Planilhas(arquivo_entrada, arquivo_saida)
    except (IndexError, ValueError):
        print("Uso: python main.py arquivo_entrada.xlsx relatorio_gerado.csv")
    except (FileNotFoundError):
        print(f"Caminho {arquivo_entrada} inacessivel ou caminho {arquivo_saida} inexistente")
    except (zipfile.BadZipFile):
        print(f"Arquivo {arquivo_entrada} invalido. Esperado XLSX")
    except:
        print("Falha ao converter para CSV")
        sys.exit(1)
