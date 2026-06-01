# ========================================================================
# Miniprojeto Módulo 01
# Autor: Dionicio Rosales
# Turma: QA VDBI 2026/1 2   (T1)
# ========================================================================

# ====================  importação de bibliotecas ====================
import pandas as pd

# ==================== Carregar dataset Varejo.csv ====================
def carregar_dados(caminho,type):
    df=[]
    
    if type=="csv":
        df=pd.read_csv(caminho,sep=';')
    else:
        print("formato inválido")

    return df

# ==================== Reportar informações do dataset Varejo.csv original ====================
def descrever_dados(df):
# reportando informações do dataset original
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

# ==================== Verificar e reportar problemas =======================
# verifica a quantidade e porcentagem de valores nulos por coluna
def verifica_nulosxcoluna(df):
    print("Quantidade de valores nulos por coluna: ")
    print(df.isnull().sum())

    print("Porcentagem de valores nulos por coluna: ")
    print( (df.isnull().mean() * 100).round(2))
    print("\n")

# Verificar e reportar quantidade de linhas duplicadas
def verifica_duplicatas(df):
    qtd_duplicadas = df.duplicated().sum()    
    print(f"Quantidade de linhas duplicadas: {qtd_duplicadas}")
    print("\n")

# Verificar e reportar colunas com problemas no nome ex: Unnamed
def inconsistencia_nome_coluna(df):
    print([col for col in df.columns if 'Unnamed' in str(col)])

# Verificar e reportar quantidade de datas inválidas
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
    

# ==================== Etapas de Limpeza ====================

def padroniza_valores_numericos(df, colunas_num):
    for coluna in colunas_num:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
        df[coluna] = df[coluna].round()
        df[coluna] = df[coluna].astype("Int64")

    return df

def padroniza_valores_texto(df, colunas_str):
    for coluna in colunas_str:
        df[coluna] = df[coluna].astype(str).strip().replace(" ", "", regex=False).upper()

    return df

def padroniza_datas(df, colunas_datas):
    for coluna in colunas_datas:
        df[coluna] = pd.to_datetime(df[coluna], format="%d/%m/%Y", errors="coerce")

    return df

def padronizar_tipos_dados(df):
    colunas_num=["CO_ID","CL_ID","CL_FHL","PD_ID"]
    df = padroniza_valores_numericos(df,colunas_num)
    print("Valores numericos padronizados para inteiros.")

    # CL_EC: Estado civil é uma categoria representada por numeros. Consideramos como str
    colunas_str = ["CL_GENERO","CL_EC","CL_SEG","PR_CAT","PR_NOME"]
    df = padroniza_valores_texto(df, colunas_str)
    print("Valores texto padronizados para maiúsculo e sem espaço em branco.")
    
    colunas_datas=["DATA"]
    df = padroniza_datas(df, colunas_datas)

    print()

def remover_imputar_nulos(df):

    return df

def eliminar_duplicatas(df):

    return df

# remover ou imputar nulos (explique a escolha), eliminar duplicatas relevantes e ajustar tipos de dados (ex.: converter coluna DATA para datetime).
def limpeza_dados(df):
    df=padronizar_tipos_dados(df)
    df=remover_imputar_nulos(df)
    df=eliminar_duplicatas(df)


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