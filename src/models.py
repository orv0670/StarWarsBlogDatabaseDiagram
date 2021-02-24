import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color =Column(String(250), nullable=False)
    skin_color =Column(String(250), nullable=False)
    eye_color =Column(String(250), nullable=False)
    birth_year =Column(String(250), nullable=False)
    gender =Column(String(250), nullable=False)
    created =Column(String, nullable=False)
    edited =Column(String, nullable=False)
    name =Column(String(250), nullable=False)
    homeworld =Column(String(250), nullable=False)
    url =Column(String(250), nullable=False)

class planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer,primary_key=True)
    climate =Column(String(250), nullable=False)
    created =Column(String, nullable=False)
    diameter = Column(Integer, nullable=False)
    edited =Column(String, nullable=False)
    gravity =Column(String(250), nullable=False)
    name =Column(String(250), nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    surface_water = Column(Integer, nullable=False)
    terrain =Column(String(250), nullable=False)
    url =Column(String(250), nullable=False)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    user_name =Column(String(250), nullable=False)
    contraseña =Column(String(250), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id_personaje = Column(Integer, ForeignKey('personajes.id'),primary_key=True)
    id_planeta = Column(Integer, ForeignKey('planetas.id'),primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'),primary_key=True)
    nombre_favorito_personaje =Column(String(250), ForeignKey('personajes.name'),nullable=False)
    nombre_favorito_planetas =Column(String(250), ForeignKey('planetas.name'),nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')