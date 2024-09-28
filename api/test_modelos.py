from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "./MachineLearning/data/test_dataset_tea.csv"
colunas = ['a1_score', 'a2_score', 'a3_score', 'a4_score', 'a5_score', 'a6_score', 'a7_score', 'a8_score', 'a9_score', 'a10_score', 'gender_cod', 'jaundice_cod', 'autism_cod', 'relation_cod', 'class']

# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)
array = dataset.values
X = array[:,0:-1]
y = array[:,-1]
    
# Método para testar pipeline Random Forest a partir do arquivo correspondente
def test_modelo_rf():
    # Importando pipeline de Random Forest
    rf_path = './MachineLearning/pipelines/rf_tea_pipeline.pkl'
    modelo_rf = Pipeline.carrega_pipeline(rf_path)

    # Obtendo as métricas do Random Forest
    acuracia_rf = Avaliador.avaliar(modelo_rf, X, y)
    
    # Testando as métricas do Random Forest
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_rf >= 0.78
    # assert recall_rf >= 0.5 
    # assert precisao_rf >= 0.5 
    # assert f1_rf >= 0.5
    

