from datetime import date
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///produktai_receptai.db")
Base = declarative_base()



class TurimasProduktas(Base):
    __tablename__ = "turimi_produktai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    kiekis = Column("Produkto kiekis", Float)
    produktas_id = Column(Integer, ForeignKey("produktas.id"))
    produktas = relationship("Produktas")
    
    def __repr__(self):
        return f"{self.produktas_id} yra tiek  - {self.kiekis}"

class Produktas(Base):
    __tablename__ = "produktas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas = Column("Produkto pavadinimas", String)
    mato_vnt = Column("Matuojamas", String)
    
    def __repr__(self):
        return f"{self.id} {self.pavadinimas} matuojama {self.mato_vnt}"

class ProduktasRecepte(Base):
    __tablename__ = "produktas_recepte"
    id = Column(Integer, primary_key=True, autoincrement=True)
    kiekis = Column("Produkto kiekis", Float)
    produktas_id = Column(Integer, ForeignKey("produktas.id"))
    receptas_id = Column(Integer, ForeignKey("receptai.id"))
    produktas = relationship("Produktas")
    receptas = relationship("Receptas")

    def __repr__(self):
        return f"{self.produktas_id} {self.kiekis}"

class Receptas(Base):
    __tablename__ = "receptai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pavadinimas = Column("Recepto pavadinimas", String)

    def __repr__(self):
        return f"{self.id} {self.pavadinimas}"
    
Base.metadata.create_all(engine)

