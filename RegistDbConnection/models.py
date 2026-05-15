"""
 pip install cryptography
 pip install pymysql
 pip install sqlalchemy

"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
#  Creamos el objeto que nos permite gestionar la creacion de las tablas a partir de los modelos

Base = declarative_base()

class Cliente(Base):
    # Creamos la tabla
    __tablename__ = "clientes"
    # Creamos los atributos del objeto cliente y definimos el tipo de dato para la base de datos
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    telefono = Column(String(20))

    # Ya que se quiere una interconexion entre el cliente y sus pedidos, creamos un campo especial que sirve como punto de conexion.
    # Al backpopulates indica el atributo del modelo Pedido con el cual se enlazara el atributo
    # Los valores en cascade indican la eliminacion del los pedidos cuando su Cliente se elimne, para evitar pedidos sin cliente.
    pedidos = relationship("Pedido", back_populates='cliente', cascade='all, delete-orphan')

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    # Este campo se conecta con el id del cliente para usarlo como llave externa
    cliente_id = Column(Integer, ForeignKey("clientes.id")) 

    # Al igual que el atributo pedidos del Cliente, este campo se conecta con el atributo pedidos del modelo usuario
    cliente = relationship("Cliente", back_populates="pedidos")

