from crud import *

inicializar_db()

while True:
    seleccion = input("Seleccione una opcion:\n1. Crear usuario\n2. Listar clientes\n3. Crear pedido\n5. Salir\n:")

    match seleccion:
        case '1':
            print("Creando usuario")
            registrar_cliente(input("Ingrese el nombre"), input("Ingrese la ciudad"))

        case '2':
            print("Lista de clientes")
            print("-"*50)
            clientes = listaClientes()
            for cliente in clientes:
                print(f"{cliente.nombre} \t {cliente.ciudad}")
            print("-"*50)

        case '3':
            print("Lista de clientes")
            clientes = listaClientes()
            for cliente in clientes:
                print(f"{cliente.nombre} \t {cliente.ciudad}")
            print("-"*50)
            print("-"*50)

            id = input("Seleccione el id del cliente para realizar el pedido: ")
            registrar_pedido(
                id,
                input("Platillo deseado: "), 
                input("Tipo de platillo: "),
                float(input("Precio del platillo: ")), 
                int(input("Cantidad: "))
            )
        case '5':
            print("Fin del programa")
            exit()
        case _:
            print("No existe la opcion seleccionada")
        
    print("------------------------------------------")