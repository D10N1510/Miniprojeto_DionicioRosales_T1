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

# Padronizar valores numericos para Int64
def padroniza_valores_numericos(df, colunas_num):
    for coluna in colunas_num:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
        df[coluna] = df[coluna].round()
        df[coluna] = df[coluna].astype("Int64")

    return df

# Padronizar valores texto para maiúsculo e sem espaços
def padroniza_valores_texto(df, colunas_str):
    for coluna in colunas_str:
        df[coluna] = df[coluna].astype(str).str.strip().str.upper()

    return df

# Padronizar datas validas para tipo datetime e inválidas pra nulo
def padroniza_datas(df, colunas_datas):
    for coluna in colunas_datas:
        df[coluna] = pd.to_datetime(df[coluna], format="%d/%m/%Y", errors="coerce")

    return df

def padronizar_tipos_dados(df):
    colunas_num=["CO_ID","CL_ID","CL_FHL","PR_ID"]
    df = padroniza_valores_numericos(df,colunas_num)
    print("Valores numericos padronizados para inteiros.")

    # CL_EC: Estado civil é uma categoria representada por numeros. Consideramos como str
    colunas_str = ["CL_GENERO","CL_EC","CL_SEG","PR_CAT","PR_NOME"]
    df = padroniza_valores_texto(df, colunas_str)
    print("Valores texto padronizados para maiúsculo e sem espaço em branco.")
    
    colunas_datas=["DATA"]
    df = padroniza_datas(df, colunas_datas)
    print("Valores de datas padronizadas pra tipo datetime. Datas inválidas são atribuidas como valor nulo")

    return df

# Remover linhas com valores nulos em qualquer coluna
def remover_nulos(df):
    df = df.dropna()
    print("Removendo linhas que possuem qualquer valor nulo em alguma coluna.")

    return df

# remover linhas duplicadas e manter a primeira ocorrência
def eliminar_duplicatas(df):
    df = df.drop_duplicates(keep="first")

    return df

# Imputar o valor "SEM-CATEGORIA" pro valor #N/D encontrado na coluna PR_CAT
def imputar_valores(df):    
    print(df["PR_CAT"].unique())
    # ['BEBIDAS', 'HIGIENE', 'ALIMENTOS', 'LIMPEZA', 'ACESSORIOS', 'PET', '#N/D']
    # imputar o valor SEM_CATEGORIA pra #N/D
    df.loc[df["PR_CAT"]=='#N/D',"PR_CAT"] = "SEM-CATEGORIA"
    print(df["PR_CAT"].unique())

    return df

# remover nulos, eliminar duplicatas relevantes e ajustar tipos de dados.
def limpeza_dados(df):
    # selecionar colunas com valores validos (10 primeiras)
    colunas = df.columns
    colunas = colunas[0:10]
    print(f"Colunas validas {colunas}")
    df = df[colunas]
    df = padronizar_tipos_dados(df)
    df = remover_nulos(df)
    df = eliminar_duplicatas(df)
    df = imputar_valores(df)

    return df


# ========================== Gerar estatísticas descritivas ========================== 
# Para coluna de número de filhos do cliente CL_FHL (média; mediana; desvio padrão; moda; máximo; mínimo; e contagem).
def estatistica_coluna_específica(df , coluna_especifica):
    valor_media = df[coluna_especifica].mean()
    valor_std =  df[coluna_especifica].std()
    valor_moda = df[coluna_especifica].mode()
    valor_maximo = df[coluna_especifica].max()
    valor_minimo = df[coluna_especifica].min()
    valor_contagem = df[coluna_especifica].sum()

    print(f"Estatísticas da coluna {coluna_especifica}")
    print(f"Valor da média {valor_media}")
    print(f"Valor da moda {valor_moda}")
    print(f"Valor do desvio padrão {valor_std}")
    print(f"Valor da mínimo {valor_minimo}")
    print(f"Valor da máximo {valor_maximo}")
    print(f"Soma total (contagem) {valor_contagem}")


# ============================ Explorar padrões de agrupamento ============================
# Com pelo menos dois agrupamentos (por exemplo: gênero com mais vendas, compras), usando groupby() ou pivot_table().

def reporta_agrupamentos(df):

    # quantidade de vendas por categoria
    contagem = df.groupby(df["PR_CAT"]).size()
    print(contagem.sort_values())
    # categoria que mais vendeu foi ALIMENTOS

    # quantidade de vendas por genero
    contagem = df.groupby(df["CL_GENERO"]).size()
    print(contagem.sort_values())
    # GENERO que mais comprou foi F

    # quantidade de vendas por estado civil
    # 1:Casado ou uniao estavel, 2:Divorciado, 3:Separado, 4:Solteiro 5:Viuvo
    contagem = df.groupby(df["CL_EC"]).size()
    print(contagem.sort_values())
    # ESTADO CIVIL que mais comprou foi 3 (Separado)

# ====================================================
# Produzir um pequeno bloco de conclusões com os principais insights obtidos e possíveis problemas remanescentes na base.
def reporta_conclusoes(df):
    print (" ================== CONLCUSOES ===========================")
    print(" 1.- Categoria (PR_CAT) que mais vendeu foi ALIMENTOS.")
    print(" 2.- GENERO (CL_GENERO) que mais comprou foi F (Feminino).")
    print(" 3.- ESTADO CIVIL (CL_EC) que mais comprou foi 3 (Separado).")
    print("A base ainda tem 3228 linhas com valores SEM_CATEGORIA.")

def salvar_arquivo_limpo(df, caminho_salvar):
    df.to_csv(caminho_salvar, index=False, sep=';', encoding='utf-8-sig')
    print(f"Dataset limpo salvo com sucesso.!")

def main():
    caminho = "data/Varejo.csv"
    df = carregar_dados(caminho,"csv")
    descrever_dados(df)
    reportar_problemas(df)
    df = limpeza_dados(df)
    coluna_especifica = "CL_FHL"
    estatistica_coluna_específica(df , coluna_especifica)
    reporta_agrupamentos(df)
    reporta_conclusoes(df)
    caminho_salvar = "data/Varejo_limpo.csv"
    salvar_arquivo_limpo(df, caminho_salvar)

if __name__ == '__main__':
    main()