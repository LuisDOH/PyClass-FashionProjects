from sqlalchemy import create_engine
import pandas as pd

# # Informacion de la base de datos ===================================
usuarioDb = "appuser"
passwordDb = '123456'
ip = "192.168.1.5"
db = "test_app"
# Creacion de parametros de conexion 
url =  f"mysql+pymysql://{usuarioDb}:{passwordDb}@{ip}:3306/{db}"
# ==================================================================

engine = create_engine(url)

query_pedidos = """
        SELECT * FROM pedidos;
"""
query_clientes = "SELECT * FROM clientes;"

# Hacemos la peticion a traves de pandas
with engine.connect() as conection:
    df_pedidos = pd.read_sql_query(query_pedidos, con=conection)
    df_clientes = pd.read_sql_query(query_clientes, con=conection)

print(df_pedidos.head(20))
print(df_clientes.head(20))
print(df_pedidos.info())
print(df_clientes.info())

"""
df_limpio = df.dropna()
df_limpio = df.dropna(how='all')
# Elimina la fila solo si 'producto' o 'precio' están nulos
df_limpio = df.dropna(subset=['producto', 'precio'])
# Cambiar los nulos en la columna 'ciudad' por 'No Especificado'
df['ciudad'] = df['ciudad'].fillna('No Especificado')

# .dayofweek o .weekday devuelven un entero del 0 al 6
df['dia_semana_num'] = df['fecha'].dt.dayofweek

# Devuelve 'Monday', 'Tuesday', etc.
df['dia_semana_nombre'] = df['fecha'].dt.day_name()

dias_espanol = {
    'Monday': 'Lunes', 'Tuesday': 'Martes', 'Wednesday': 'Miércoles',
    'Thursday': 'Jueves', 'Friday': 'Viernes', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
}

# Primero extraes el nombre y luego lo traduces
df['dia_semana_espanol'] = df['fecha'].dt.day_name().map(dias_espanol)

df['mes_num'] = df['fecha'].dt.month


-- RENOMBRADO DE COLUMNAS ---
# Cambiamos 'id' por 'id_cliente' y 'precio' por 'precio_unitario'
df_renombrado = df.rename(columns={
    'id': 'id_cliente',
    'precio': 'precio_unitario'
})

MODIFIAR EL MISMO DF (inplace)
df.rename(columns={'id': 'id_cliente'}, inplace=True)

BUSQUEDA y REEMPLAZO 
# "Busca en el DataFrame donde el nombre sea 'Alejandro Gómez', ve a la columna 'ciudad' y cámbiala por 'Bogotá'"

df.loc[df['nombre'] == 'Alejandro Gómez', 'ciudad'] = 'Bogotá'

# Cambiar la ciudad del cliente con ID 10
df.loc[df['cliente_id'] == 10, 'ciudad'] = 'Buenos Aires'

# Reemplaza un valor específico por otro en toda la columna 'ciudad'
df['ciudad'] = df['ciudad'].replace('CDMX', 'Ciudad de México')
"""

# Iniciamos con opearaciones simples "CREANDO NUEVAS COLUMNAS"
df_pedidos["monto total"] = df_pedidos["precio"] * df_pedidos["cantidad"]
df_pedidos["mes"] = df_pedidos["fecha"].dt.strftime("%Y-%m")

print(df_pedidos.head())

# FUSION DE DATOS
# La union se realiza siguiendo el patro de join comun de SQL
df_master = pd.merge(df_pedidos, df_clientes, left_on="cliente_id", right_on="id", suffixes=('_platillo', '_cliente'))
# Eliminamos la columna id duplicada para mantener limpio el DataFrame
df_master = df_master.drop(columns=['id_cliente'])

print(df_master.head())

"""
    La siguiente operacion natural es buscar que productos nos generan mas ganancias o saber cuales son los productos mas vendidos

    *** AGREGACION
    Una de las operaciones mas utiles es la agregacion
    Que se puede realizar de tres formas fundamentales
    df.groupby('columna_llave')['columna_valor'].num_agregacion()



"""
# Platillos de mayor venta
top_platillos = df_master.groupby('producto')['monto total'].sum()#.sort_values(by="monto total", ascending=False)
print(top_platillos.head())

# Que pasa si necesitamos varias operaciones
platillos_info = df_master.groupby('producto')['monto total'].agg(['sum', 'mean', 'count', 'mean', 'median', 'std','var', 'max']).sort_values(by="sum", ascending=False)

print(platillos_info.head())

# Si queremos tener la opcion de una agregacion con encabezados y ordenamiento
top_platillos = df_master.groupby('producto').agg(monto_vendido = ('monto total', 'sum')).sort_values(by="monto_vendido", ascending=False)
print(top_platillos.head())

# Agregacion multiple
top_productos = df_master.groupby('producto').agg(
    unidades_vendidas=('cantidad', 'sum'),
    ingresos_totales=('monto total', 'sum')
).sort_values(by='ingresos_totales', ascending=False)


print("--- TOP 5 PRODUCTOS POR INGRESO ---")
print(top_productos.head(5))

# Agrupacion multiple con multiples operaciones
analisis_ciudad = df_master.groupby('ciudad').agg(
    total_ventas=('monto total', 'sum'),
    ordenes_totales=('cliente_id', 'count'),
    ticket_promedio=('monto total', 'mean')
).sort_values(by='total_ventas', ascending=False)

print("\n--- DESEMPEÑO POR CIUDAD ---")
print(analisis_ciudad)

# Tendencia mensual del cliente
tendencia_mensual = df_master.groupby('mes').agg(utilidad = ('monto total', sum)).sort_values("mes", ascending=True)
print("--- TENDENCIA MENSUAL ---")
print(tendencia_mensual)

# Comportamiendo del cliente
perfil_clientes = df_master.groupby('nombre'). agg(visitas = ('fecha', 'count'), gastado = ("monto total", 'sum')).sort_values('gastado', ascending=False)
print("Perfil de clientes")
print(perfil_clientes)


# Creacion de graficos 
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Creamos la figura y definimos el tamaño (Ancho, Alto)
plt.figure(figsize=(10, 5))

# 2. Graficamos usando Seaborn (usamos las primeras 5 filas del análisis anterior)
sns.barplot(
    data=perfil_clientes.head(5).reset_index(), 
    x='nombre', 
    y='gastado', 
    palette='viridis' # Paleta de colores degradada y profesional
)

# Añadir etiquetas de datos (opcional, para ver el número exacto sobre cada punto)
for x, y in zip(perfil_clientes.head(5).reset_index()['nombre'], perfil_clientes['gastado']):
    plt.text(x, y + (y*0.02), f"${y:,.0f}", ha='center', fontsize=9, fontweight='bold')

# 3. Personalización de etiquetas
plt.title('Top Clientes', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Clientes', fontsize=12)
plt.ylabel('$ Consumo', fontsize=12)

# 4. Ajuste automático y visualización
plt.tight_layout()
plt.show()

# Tendencia mensual

plt.figure(figsize=(10,5))
sns.lineplot(
    data=tendencia_mensual.reset_index().sort_values("mes", ascending=True),
    x = "mes",
    y = "utilidad", 
    marker='o', 
    linewidth = 2.5, 
    color = "#2b5c8f"
)

# agregando etiquetas
for x,y in zip(tendencia_mensual.reset_index().sort_values("mes", ascending=True)["mes"], tendencia_mensual["utilidad"]):
    plt.text(x,y+y*0.02, f"{y:,.0f}", ha='center', fontsize = 9, fontweight="bold")

plt.title("Evolucion mensual")
plt.xlabel('Periodo (Año-Mes)', fontsize=12)
plt.ylabel('Ingresos ($)', fontsize=12)
plt.ylim(0, tendencia_mensual['utilidad'].max() * 1.15) # Da un 15% de margen arriba para que no se corten las etiquetas

plt.tight_layout()
plt.show()