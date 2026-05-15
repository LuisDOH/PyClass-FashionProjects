from database import *
print("Bienvenidos")

inicializar_db()

while True:
    seleccion = input("Seleccione una opcion:\n1. Crear usuario\n2. Modificar Usuario\n3. Crear Pedido\n4. Eliminar Usuario\n5. Salir\n:")

    match seleccion:
        case '1':
            print("Registro de usuario")
            nombre = input("Nombre del cliente: ")
            telefono = input("Numero Telefonico: ")
            id = crearUsuario(nombre, telefono)
            print(f"Usuario Creado con el id {id}")


        case '2':
            clientes = listaClientes()
            print("-"*55)
            for cliente in clientes:
               print(f"{cliente.id}\t{cliente.nombre}\t\t{cliente.telefono}\t{len(cliente.pedidos)}")
            print("-"*55)

            id = int(input("Seleccione el ID del cliente que desea modificar: "))
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo telefono: ")

            result = modificarCliente(id, nombre, telefono)

            if result == True:
                print("Usuario Modificado con exito")
            else:
                print("Usuario no encontrado ")

        case '3':
            clientes = listaClientes()
            print("-"*55)
            for cliente in clientes:
               print(f"{cliente.id}\t{cliente.nombre}\t\t{cliente.telefono}\t{len(cliente.pedidos)}")
            print("-"*55)

            id = int(input("Seleccione el ID del cliente para realizar el pedido: "))

            # Se buscan los platillos actuales solicitados por el cliente
            platillos = obtener_pedidos_cliente(id)
            print(platillos)

            # Se pide el nombre del platillo
            nombre = input("Platillo: ")
            # Se crea el platillo
            crearPedido(id, nombre)

        case '4':
            clientes = listaClientes()
            print("-"*55)
            for cliente in clientes:
               print(f"{cliente.id}\t{cliente.nombre}\t\t{cliente.telefono}\t{len(cliente.pedidos)}")
            print("-"*55)

            id = int(input("Seleccione el ID del cliente que desea eliminar: "))
            eliminar_cliente(id)

        case '5':
            print("Fin del programa")
            exit()
        case _:
            print("No existe la opcion seleccionada")
        
    print("------------------------------------------")