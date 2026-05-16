from sqlalchemy.orm import Session
from models2 import Cliente, Pedido, Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from datetime import date as fecha, timedelta


# Informacion de la base de datos ===================================
usuarioDb = "appuser"
passwordDb = '123456'
ip = "192.168.1.5"
db = "test_app"
# Creacion de parametros de conexion 
url =  f"mysql+pymysql://{usuarioDb}:{passwordDb}@{ip}:3306/{db}"
# ==================================================================


import random
def get_random_date(start_date, end_date):
    # calucilamos la difererncia entre la fecha fin y la fecha inicio
    delta = end_date - start_date
    # tomamos un valor randon desde cero hasta la fecha en dias de la diferencia de fechas
    random_days = random.randrange(delta.days)
    # Sumamos la cantidad de dias a la fecha de inicio
    return start_date + timedelta(days=random_days)


# Se crea una entidad encargada de realizar la conexion con la base de datos
engine = create_engine(url)
# Se crea una entidad encargada de gestionar las operaciones con la base de datos
sesion = sessionmaker(bind=engine)

# Se genera la base de datos en caso de requerirse usando los modelos
def inicializar_db():
    Base.metadata.create_all(engine)


# Función para registrar un cliente
def registrar_cliente(nombre: str, ciudad: str):
    nuevo = Cliente(nombre=nombre, ciudad=ciudad)
    with sesion() as sess:
        sess.add(nuevo)
        sess.commit()
        return nuevo
    
def listaClientes():
    with sesion() as sess:
        clientes = sess.query(Cliente).all()
        #clientes = sess.query(Cliente).options(joinedload(Cliente)).all()
        return clientes
    


# Función para registrar un pedido
def registrar_pedido(cliente_id: int, prod: str, cat: str, precio: float, cant: int):
    ini = fecha(2020, 1, 1)
    end = fecha(2026,5,15)
    date = get_random_date(ini, end)
    pedido = Pedido(cliente_id=cliente_id, producto=prod, categoria=cat, precio=precio, cantidad=cant, fecha = date)
    with sesion() as sess:
        sess.add(pedido)
        sess.commit()
        return pedido

# Función para ver todo (Lo que Pandas leerá después)
def obtener_todos_los_pedidos(db: Session):
    return db.query(Pedido).all()