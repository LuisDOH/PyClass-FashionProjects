from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    ciudad = Column(String(100))  # Útil para análisis geográfico
    
    # Conexión con los pedidos
    pedidos = relationship("Pedido", back_populates='cliente', cascade='all, delete-orphan')

class Pedido(Base):
    __tablename__ = "pedidos"
    
    id = Column(Integer, primary_key=True)
    producto = Column(String(150), nullable=False)
    categoria = Column(String(50))    # Para análisis de "Top Categorías"
    precio = Column(Float, nullable=False) # Para sumatorias y promedios
    cantidad = Column(Integer, default=1)
    fecha = Column(DateTime, default=datetime.now) # Para series de tiempo
    
    # Llave foránea para conectar con el Cliente
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", back_populates="pedidos")