from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "Maria"
    a1_score: int = 0
    a2_score: int = 0
    a3_score: int = 0
    a4_score: int = 0
    a5_score: int = 0
    a6_score: int = 0
    a7_score: int = 0
    a8_score: int = 0
    a9_score: int = 0
    a10_score: int = 0
    gender_cod: int = 0
    jaundice_cod: int = 0
    autism_cod: int = 0
    relation_cod: int = 0 
    
class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "Maria"
    a1_score: int = 0
    a2_score: int = 0
    a3_score: int = 0
    a4_score: int = 0
    a5_score: int = 0
    a6_score: int = 0
    a7_score: int = 0
    a8_score: int = 0
    a9_score: int = 0
    a10_score: int = 0
    gender_cod: int = 0
    jaundice_cod: int = 0
    autism_cod: int = 0
    relation_cod: int = 0 
    outcome: int = None
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Maria"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Maria"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "name": paciente.name,
        "a1_score": paciente.a1_score,
        "a2_score": paciente.a2_score,
        "a3_score": paciente.a3_score,
        "a4_score": paciente.a4_score,
        "a5_score": paciente.a5_score,
        "a6_score": paciente.a6_score,
        "a7_score": paciente.a7_score,
        "a8_score": paciente.a8_score,
        "a9_score": paciente.a9_score,
        "a10_score": paciente.a10_score,
        "gender_cod": paciente.gender_cod,
        "jaundice_cod": paciente.jaundice_cod,
        "autism_cod": paciente.autism_cod,
        "relation_cod": paciente.relation_cod,
        "outcome": paciente.outcome
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "name": paciente.name,
            "a1_score": paciente.a1_score,
            "a2_score": paciente.a2_score,
            "a3_score": paciente.a3_score,
            "a4_score": paciente.a4_score,
            "a5_score": paciente.a5_score,
            "a6_score": paciente.a6_score,
            "a7_score": paciente.a7_score,
            "a8_score": paciente.a8_score,
            "a9_score": paciente.a9_score,
            "a10_score": paciente.a10_score,
            "gender_cod": paciente.gender_cod,
            "jaundice_cod": paciente.jaundice_cod,
            "autism_cod": paciente.autism_cod,
            "relation_cod": paciente.relation_cod,
            "outcome": paciente.outcome
        })

    return {"pacientes": result}

