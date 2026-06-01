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
    print(df.info())
    print(df.shape)
    print(df.head())
    print(df.columns)

# Verificar e reportar problemas 
# valores nulos por coluna, duplicatas e possíveis inconsistências (ex.: datas inválidas ou categorias vazias).



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

if __name__ == '__main__':
    main()