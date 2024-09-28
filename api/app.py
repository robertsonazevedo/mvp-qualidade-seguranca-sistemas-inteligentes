from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Adição, visualização, remoção e predição de pacientes com TEA")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de pacientes
@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_pacientes():
    """Lista todos os pacientes cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os pacientes")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        # Se não houver pacientes
        return {"pacientes": []}, 200
    else:
        logger.debug(f"%d pacientes encontrados" % len(pacientes))
        print(pacientes)
        return apresenta_pacientes(pacientes), 200


# Rota de adição de paciente
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PacienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    
    Args:
        name: nome do paciente
        a1_score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        a2_score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        A3_Score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        a4_score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        a5_score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        a6_score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        A7_score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        a8_score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        a9_score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        a10_score: 0 - Para pontos até 32. 1 - Para pontos de 33 em diante, máximo 50.
        gender_cod: Genero (0 - Masculino | 1 - Feminino)
        jaundice_cod: Se teve Icterícia ao nascer (0 - Não | 1 - Sim)
        autism_cod: Se tem pais com diagnóstico de autismo (0 - Não | 1 - Sim)
        relation_cod: quem preencheu o formulário (0 - Próprio | 1 - Pais | 2 - Parentes | 3 - Cuidador | 4 - Outros)
        outcome: diagnóstico (0 - Tea não confirmado | 1 - Tea Confirmado)
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    # TODO: Instanciar classes

    # Recuperando os dados do formulário
    name = form.name
    a1_score = form.a1_score
    a2_score = form.a2_score
    a3_score = form.a3_score
    a4_score = form.a4_score
    a5_score = form.a5_score
    a6_score = form.a6_score
    a7_score = form.a7_score
    a8_score = form.a8_score
    a9_score = form.a9_score
    a10_score = form.a10_score
    gender_cod = form.gender_cod
    jaundice_cod = form.jaundice_cod
    autism_cod = form.autism_cod
    relation_cod = form.relation_cod
        
    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    # Carregando modelo
    model_path = './MachineLearning/pipelines/rf_tea_pipeline.pkl'
    # modelo = Model.carrega_modelo(ml_path)
    modelo = Pipeline.carrega_pipeline(model_path)
    # Realizando a predição
    outcome = int(Model.preditor(modelo, X_input)[0])
    
    paciente = Paciente(
        name=name,
        a1_score = a1_score,
        a2_score = a2_score,
        a3_score = a3_score,
        a4_score = a4_score,
        a5_score = a5_score,
        a6_score = a6_score,
        a7_score = a7_score,
        a8_score = a8_score,
        a9_score = a9_score,
        a10_score = a10_score,
        gender_cod = gender_cod,
        jaundice_cod = jaundice_cod,
        autism_cod = autism_cod,
        relation_cod = relation_cod,
        outcome = outcome
    )
    logger.debug(f"Adicionando paciente de nome: '{paciente.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(Paciente).filter(Paciente.name == form.name).first():
            error_msg = "Paciente já existente na base :/"
            logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
        return apresenta_paciente(paciente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo paciente :/"
        logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de paciente por nome
@app.get('/paciente', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):    
    """Faz a busca por um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    paciente_nome = query.name
    logger.debug(f"Coletando dados sobre paciente #{paciente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente {paciente_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar paciente '{paciente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{paciente.name}'")
        # retorna a representação do paciente
        return apresenta_paciente(paciente), 200
   
    
# Rota de remoção de paciente por nome
@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
    """Remove um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    paciente_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre paciente #{paciente_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        error_msg = "Paciente não encontrado na base :/"
        logger.warning(f"Erro ao deletar paciente '{paciente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        logger.debug(f"Deletado paciente #{paciente_nome}")
        return {"message": f"Paciente {paciente_nome} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)