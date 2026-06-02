
# Mini-Projeto Avaliativo - Módulo 1

* **Nome:** Dionicio Angel Vasquez Rosales
* **Turma:** T1

## Tecnologias
* Python 3.13.0
* Pandas
* CSV
* Github

## Como executar
* Baixar projeto como zip ou clonar o repositorio
* Instalar dependencias: pip install -r requirements.txt
* Disponibilizar a base "Varejo.csv" na pasta "data"
* Executar o arquivo script_DionicioRosales_T1.py

## Insights obtidos
Após aplicar a análise exploratória de dados (AED), se obteve os seguintes insights:
* A Categoria (PR_CAT) que mais vendeu foi ALIMENTOS.
* Os clientes com gênero Feminino (F) foram os que mais compraram.
* CLientes com estado civil "Separado" (3) foram as que mais compraram.
* O máximo número de filhos por cliente é 4 e o mínimo é 0.
* O valor médio do número de filhos por cliente é 1.

## Problemas remanescentes no dataset após AED
* A base ainda tem 3228 linhas com valores SEM-CATEGORIA que precisam de revisão.

## Principais passos da AED aplicados:
* Carregamento e descrição de informações da base original.
* Reporte de problemas como: valores nulos por coluna, linhas duplicadas, problemas no nome da coluna, datas inválidas.
* Limpeza e padronização de dados: padronização de dados numericos, texto e datas, remoção de nulos, remoção de duplicatas, e imputação de valores.
* Calculo de estatisticas básicas para a coluna que contem o número de filhos por cliente.
* Aplicação de agrupamentos usando groupby para as colunas PR_CAT, CL_GENERO e CL_EC para obter a quantidade de vendas por categoria, genero e estado civil, respectivamente. 

## Resultado do AED
Após executar o arquivo .py, o arquivo "Varejo_limpo.csv" contendo a base limpa é salva na pasta dados.

