from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Name,A1_Score,A2_Score,A3_Score,A4_Score,A5_Score,A6_Score,A7_score,A8_score,A9_score,A10_score,Gender_Cod,Jaundice_Cod,Autism_Cod,Relation_Cod,Diagnostic

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    a1_score = Column("A1_Score", Integer)
    a2_score = Column("A2_Score", Integer)
    a3_score = Column("A3_Score", Integer)
    a4_score = Column("A4_Score", Integer)
    a5_score = Column("A5_Score", Integer)
    a6_score = Column("A6_Score", Integer)
    a7_score = Column("A7_score", Integer)
    a8_score = Column("A8_score", Integer)
    a9_score = Column("A9_score", Integer)
    a10_score = Column("A10_score", Integer)
    gender_cod = Column("Gender_Cod", Integer)
    jaundice_cod = Column("Jaundice_Cod", Integer)
    autism_cod = Column("Autism_Cod", Integer)
    relation_cod = Column("Relation_Cod", Integer)
    outcome = Column("Diagnostic", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, a1_score:int, a2_score:int, a3_score:int, name:str,
                 a4_score:int, a5_score:int, a6_score:int, 
                 a7_score:int, a8_score:int, a9_score:int, a10_score:int,
                 gender_cod:int, jaundice_cod:int,
                 autism_cod:int, relation_cod:int,
                 outcome:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
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
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.name=name
        self.a1_score = a1_score
        self.a2_score = a2_score
        self.a3_score = a3_score
        self.a4_score = a4_score
        self.a5_score = a5_score
        self.a6_score = a6_score
        self.a7_score = a7_score
        self.a8_score = a8_score
        self.a9_score = a9_score
        self.a10_score = a10_score
        self.gender_cod = gender_cod
        self.jaundice_cod = jaundice_cod
        self.autism_cod = autism_cod
        self.relation_cod = relation_cod
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao