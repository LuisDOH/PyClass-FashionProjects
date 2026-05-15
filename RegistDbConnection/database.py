"""
    @LD-OH
    En este archivo se generan las funciones que llevan a cabo las 
    opereaciones generales de almacenamiento de registros en una base 
    de datos:
        Create
        Read
        Update
        Delete

Note que en la importacion de los modelos, tambien se importa la variable Base que se creo a partir de un declarative_base
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

# Importando los modelos creados
from models import Base, Cliente, Pedido

# Informacion de la base de datos ===================================
usuarioDb = "appuser"
passwordDb = '123456'
ip = "192.168.1.5"
db = "test_app"
# Creacion de parametros de conexion 
url =  f"mysql+pymysql://{usuarioDb}:{passwordDb}@{ip}:3306/{db}"
# ==================================================================

# Se crea una entidad encargada de realizar la conexion con la base de datos
engine = create_engine(url)
# Se crea una entidad encargada de gestionar las operaciones con la base de datos
sesion = sessionmaker(bind=engine)

# Se genera la base de datos en caso de requerirse usando los modelos
def inicializar_db():
    Base.metadata.create_all(engine)


def crearUsuario(_nombre, _telefono):
    with sesion() as s:
        nuevo =  Cliente(nombre = _nombre, telefono = _telefono)
        s.add(nuevo)
        s.commit()
        return nuevo.id

def listaClientes():
    with sesion() as s:
        usuarios = s.query(Cliente).options(joinedload(Cliente.pedidos)).all()
        return usuarios

def modificarCliente(id, nombre="None", telefono="None"):
    with sesion() as s:
        usuario = s.query(Cliente).get(id)

        if usuario:
            usuario.nombre= nombre
            usuario.telefono = telefono
            s.commit()
            return True
        
        else:
            return False

def eliminar_cliente(cliente_id):
    with sesion() as s:
        cliente = s.query(Cliente).get(cliente_id)
        if cliente:
            # SQLAlchemy eliminará también sus pedidos automáticamente 
            # si configuraste 'cascade="all, delete-orphan"' en el modelo
            s.delete(cliente)
            s.commit()
            return True
        return False
    

def crearPedido(cliente_id, _platillo):
    print("Buscando Platillo")
    platillos = obtener_pedidos_cliente(cliente_id)
    print(platillos)
    with sesion() as s:
        # Revisar que el cliente exista
        usuario =  s.query(Cliente).get(cliente_id)
        if usuario:
            nuevo_pedido = Pedido(nombre = _platillo, cliente_id=cliente_id)
            s.add(nuevo_pedido)
            s.commit()
            return True
        else:
            return False

def obtener_pedidos_cliente(cliente_id):
    with sesion() as s:
        cliente = s.query(Cliente).get(cliente_id)
        if cliente:
            # Extraemos los datos a diccionarios para que sigan disponibles 
            # fuera de la sesión (cuando el 'with' termine)
            return [p.nombre  for p in cliente.pedidos]
        return None