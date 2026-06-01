# ========================================================================
# Miniprojeto Módulo 01
# Autor: Dionicio Rosales
# Turma: QA VDBI 2026/1 2   (T1)
# ========================================================================

# importação de bibliotecas
import pandas as pd

# Carregar dataset Varejo.csv 
def carregar_dados(caminho,type):
    df=[]
    
    if type=="csv":
        df=pd.read_csv(caminho,sep=';')
    else:
        print("formato inválido")

    return df

def descrever_dados(df):
# visualizando informações iniciais do dataset

    print("="*20 + " Carregando DataFrame Original " + "="*20)
    print(df.info())
    print(df.dtypes)
    qtd_linhas_df_original = df.shape[0]
    qtd_colunas_df_original = df.shape[1]
    print(f"Total de linhas do dataframe: {qtd_linhas_df_original}")
    print(f"Total de colunas do dataframe: {qtd_colunas_df_original}")
    print("Colunas:")
    print(df.columns)
    print("Cabeçalho do dataframe: ")
    print(df.head())
    print("="*70)
    print("\n")

# Verificar e reportar problemas 
def verifica_nulosxcoluna(df):
    print("Quantidade de valores nulos por coluna: ")
    print(df.isnull().sum())

    print("Porcentagem de valores nulos por coluna: ")
    print( (df.isnull().mean() * 100).round(2))
    print("\n")


def verifica_duplicatas(df):
    qtd_duplicadas = df.duplicated().sum()    
    print(f"Quantidade de linhas duplicadas: {qtd_duplicadas}")
    print("\n")

def inconsistencia_nome_coluna(df):
    print([col for col in df.columns if 'Unnamed' in str(col)])

def inconsistencia_data_invalida(df):
    df['datas_na'] = pd.to_datetime(df['DATA'], errors='coerce')    
    linhas_data_invalidas = df['datas_na'].isnull().sum()
    print(f"Quantidade de linhas com datas inválidas: {linhas_data_invalidas}")

# valores nulos por coluna, duplicatas e possíveis inconsistências (ex.: datas inválidas ou categorias vazias).
def reportar_problemas(df):

    print("="*20 + " Reportando Problemas " + "="*20)
    # verifica nulos por coluna
    verifica_nulosxcoluna(df)
    # verifica duplicatas
    verifica_duplicatas(df)
    # possiveis inconsistencias
    inconsistencia_nome_coluna(df)
    inconsistencia_data_invalida(df)    
    print("="*60)
    


# Etapas de Limpeza 
# remover ou imputar nulos (explique a escolha), eliminar duplicatas relevantes e ajustar tipos de dados (ex.: converter coluna DATA para datetime).




# Gerar estatísticas descritivas 
# para coluna de número de filhos do cliente (média; mediana; desvio padrão; moda; máximo; mínimo; e contagem).



# Explorar padrões de agrupamento 
# com pelo menos dois agrupamentos (por exemplo: gênero com mais vendas, compras), usando groupby() ou pivot_table().


# Produzir um pequeno bloco de conclusões (3–6 tópicos) com os principais insights obtidos e possíveis problemas remanescentes na base.





def main():
    caminho = "data/Varejo.csv"
    df = carregar_dados(caminho,"csv")
    descrever_dados(df)

    reportar_problemas(df)

if __name__ == '__main__':
    main()