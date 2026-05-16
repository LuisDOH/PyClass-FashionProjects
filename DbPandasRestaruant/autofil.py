from crud import registrar_cliente, registrar_pedido


def clienentes_autofill():

    clientes_falsos = [
        {"nombre": "Alejandro Gómez", "ciudad": "Ciudad de México"},
        {"nombre": "Valentina Silva", "ciudad": "Santiago"},
        {"nombre": "Mateo Rodríguez", "ciudad": "Buenos Aires"},
        {"nombre": "Camila López", "ciudad": "Bogotá"},
        {"nombre": "Lucas Martinez", "ciudad": "Madrid"},
        {"nombre": "Sofía Fernández", "ciudad": "Monterrey"},
        {"nombre": "Diego Torrealba", "ciudad": "Concepción"},
        {"nombre": "Isabella Rossi", "ciudad": "Milán"},
        {"nombre": "Benjamin Smith", "ciudad": "Washington D.C."},
        {"nombre": "Emma Watson", "ciudad": "Londres"},
        {"nombre": "Santiago Pérez", "ciudad": "Medellín"},
        {"nombre": "Lucía Méndez", "ciudad": "Barcelona"},
        {"nombre": "Gabriel Santos", "ciudad": "São Paulo"},
        {"nombre": "Mariana Costa", "ciudad": "Río de Janeiro"},
        {"nombre": "Nicolás González", "ciudad": "Mendoza"},
        {"nombre": "Martina Díaz", "ciudad": "Valparaíso"},
        {"nombre": "Daniel Castillo", "ciudad": "Guadalajara"},
        {"nombre": "Sara Müller", "ciudad": "Berlín"},
        {"nombre": "Thomas Dubois", "ciudad": "París"},
        {"nombre": "Elena Petrov", "ciudad": "Moscú"},
        {"nombre": "Sebastian Castro", "ciudad": "Cali"},
        {"nombre": "Victoria Ruiz", "ciudad": "Sevilla"},
        {"nombre": "Samuel Wilson", "ciudad": "San Francisco"},
        {"nombre": "Chloe Brown", "ciudad": "Toronto"},
        {"nombre": "Oliver Jones", "ciudad": "Sídney"},
        {"nombre": "Mateo Salazar", "ciudad": "Puebla"},
        {"nombre": "Paula Ortiz", "ciudad": "Viña del Mar"},
        {"nombre": "Joaquín Vega", "ciudad": "Rosario"},
        {"nombre": "Natalia Herrera", "ciudad": "Barranquilla"},
        {"nombre": "Leonardo Vinci", "ciudad": "Roma"},
        {"nombre": "Andrea Flores", "ciudad": "Valencia"},
        {"nombre": "Lucas Silva", "ciudad": "Belo Horizonte"},
        {"nombre": "Mia Novak", "ciudad": "Praga"},
        {"nombre": "Liam Davies", "ciudad": "Mánchester"},
        {"nombre": "Emily Taylor", "ciudad": "Chicago"},
        {"nombre": "Diego Morales", "ciudad": "Querétaro"},
        {"nombre": "Valeria Peña", "ciudad": "Antofagasta"},
        {"nombre": "Agustín Benítez", "ciudad": "Córdoba"},
        {"nombre": "Isabel Gutiérrez", "ciudad": "Cartagena"},
        {"nombre": "Javier Navarro", "ciudad": "Bilbao"},
        {"nombre": "Aline Ferreira", "ciudad": "Campinas"},
        {"nombre": "Yuki Tanaka", "ciudad": "Tokio"},
        {"nombre": "Noah Miller", "ciudad": "Hamburgo"},
        {"nombre": "Charlotte Petit", "ciudad": "Marsella"},
        {"nombre": "Carlos Mendoza", "ciudad": "San Luis Potosí"},
        {"nombre": "Camila Vargas", "ciudad": "La Serena"},
        {"nombre": "Facundo Rossi", "ciudad": "La Plata"},
        {"nombre": "Manuela Miranda", "ciudad": "Bucaramanga"},
        {"nombre": "Pedro Almodóvar", "ciudad": "Málaga"},
        {"nombre": "Arthur Pendragon", "ciudad": "Bristol"}
    ]

    for cliente in clientes_falsos:
        # print(cliente["nombre"])
        registrar_cliente(cliente["nombre"], cliente["ciudad"])



def pedidos_autofill():

    platillos = [
    {"platillo": "Tacos al Pastor", "categoria": "Mexicana", "precio": 12.50, "cantidad": 3},
    {"platillo": "Hamburguesa con Queso", "categoria": "Fast Food", "precio": 8.99, "cantidad": 1},
    {"platillo": "Pizza Pepperoni", "categoria": "Italiana", "precio": 14.50, "cantidad": 2},
    {"platillo": "Sushi Roll California", "categoria": "Asiática", "precio": 11.20, "cantidad": 2},
    {"platillo": "Ensalada César", "categoria": "Saludable", "precio": 9.50, "cantidad": 1},
    {"platillo": "Ramen de Cerdo", "categoria": "Asiática", "precio": 13.80, "cantidad": 1},
    {"platillo": "Lasaña de Carne", "categoria": "Italiana", "precio": 12.00, "cantidad": 1},
    {"platillo": "Burrito de Pollo", "categoria": "Mexicana", "precio": 9.99, "cantidad": 2},
    {"platillo": "Papas Fritas Grandes", "categoria": "Acompañamientos", "precio": 3.50, "cantidad": 4},
    {"platillo": "Alitas BBQ", "categoria": "Snacks", "precio": 10.50, "cantidad": 2},
    {"platillo": "Pad Thai", "categoria": "Asiática", "precio": 12.90, "cantidad": 1},
    {"platillo": "Ceviche Peruano", "categoria": "Mariscos", "precio": 15.00, "cantidad": 1},
    {"platillo": "Tarta de Queso", "categoria": "Postres", "precio": 5.50, "cantidad": 2},
    {"platillo": "Pollo Frito (4 pzs)", "categoria": "Fast Food", "precio": 7.25, "cantidad": 3},
    {"platillo": "Gnocchi de Papa", "categoria": "Italiana", "precio": 11.50, "cantidad": 1},
    {"platillo": "Enchiladas Verdes", "categoria": "Mexicana", "precio": 10.80, "cantidad": 1},
    {"platillo": "Sopa Miso", "categoria": "Asiática", "precio": 4.00, "cantidad": 2},
    {"platillo": "Sandwich de Jamón y Queso", "categoria": "Cafetería", "precio": 5.00, "cantidad": 1},
    {"platillo": "Brownie con Helado", "categoria": "Postres", "precio": 6.00, "cantidad": 1},
    {"platillo": "Nuggets de Pollo (10 pzs)", "categoria": "Fast Food", "precio": 6.50, "cantidad": 2},
    {"platillo": "Poke Bowl de Salmón", "categoria": "Saludable", "precio": 14.20, "cantidad": 1},
    {"platillo": "Paella Valenciana", "categoria": "Española", "precio": 18.50, "cantidad": 1},
    {"platillo": "Empanadas de Carne", "categoria": "Latina", "precio": 2.50, "cantidad": 6},
    {"platillo": "Crepa de Nutella", "categoria": "Postres", "precio": 5.20, "cantidad": 2},
    {"platillo": "Falafel Wrap", "categoria": "Árabe", "precio": 8.50, "cantidad": 1},
    {"platillo": "Chilaquiles Rojos", "categoria": "Mexicana", "precio": 9.00, "cantidad": 2},
    {"platillo": "Spaghetti Bolognese", "categoria": "Italiana", "precio": 11.00, "cantidad": 1},
    {"platillo": "Boneless de Pollo", "categoria": "Snacks", "precio": 11.99, "cantidad": 1},
    {"platillo": "Aros de Cebolla", "categoria": "Acompañamientos", "precio": 4.00, "cantidad": 2},
    {"platillo": "Tacos de Pescado", "categoria": "Mariscos", "precio": 13.50, "cantidad": 3},
    {"platillo": "Risotto de Hongos", "categoria": "Italiana", "precio": 16.00, "cantidad": 1},
    {"platillo": "Gyros de Pollo", "categoria": "Griega", "precio": 9.20, "cantidad": 1},
    {"platillo": "Waffles con Fresa", "categoria": "Cafetería", "precio": 7.50, "cantidad": 2},
    {"platillo": "Sopa de Tomate", "categoria": "Saludable", "precio": 6.00, "cantidad": 1},
    {"platillo": "Asado de Tira", "categoria": "Carnes", "precio": 22.00, "cantidad": 1},
    {"platillo": "Quesadilla de Flor de Calabaza", "categoria": "Mexicana", "precio": 4.50, "cantidad": 3},
    {"platillo": "Hot Dog Clásico", "categoria": "Fast Food", "precio": 3.99, "cantidad": 2},
    {"platillo": "Mochi de Té Verde", "categoria": "Postres", "precio": 4.50, "cantidad": 3},
    {"platillo": "Bowl de Acai", "categoria": "Saludable", "precio": 10.00, "cantidad": 1},
    {"platillo": "Kebab de Ternera", "categoria": "Árabe", "precio": 8.80, "cantidad": 2},
    {"platillo": "Club Sandwich", "categoria": "Cafetería", "precio": 9.50, "cantidad": 1},
    {"platillo": "Milanesa con Puré", "categoria": "Latina", "precio": 12.50, "cantidad": 1},
    {"platillo": "Dumplings de Cerdo", "categoria": "Asiática", "precio": 7.80, "cantidad": 2},
    {"platillo": "Gelato de Pistacho", "categoria": "Postres", "precio": 4.80, "cantidad": 1},
    {"platillo": "Pozole Rojo", "categoria": "Mexicana", "precio": 11.00, "cantidad": 1},
    {"platillo": "Pizza Margarita", "categoria": "Italiana", "precio": 12.50, "cantidad": 1},
    {"platillo": "Costillas BBQ", "categoria": "Carnes", "precio": 19.99, "cantidad": 1},
    {"platillo": "Hummus con Pan Pita", "categoria": "Árabe", "precio": 6.50, "cantidad": 1},
    {"platillo": "Churros con Chocolate", "categoria": "Postres", "precio": 5.00, "cantidad": 2},
    {"platillo": "Salmón a la Plancha", "categoria": "Saludable", "precio": 17.50, "cantidad": 1}
]
    import random
    for i in range(250):
        index = random.randint(0,49)
        id = random.randint(1,51)
        print(index)
        print(f"{platillos[index]["platillo"]} -- {id}")

        registrar_pedido(id, platillos[index]["platillo"],
                    platillos[index]["categoria"], 
                    platillos[index]["precio"], 
                    platillos[index]["cantidad"])


# clienentes_autofill()
pedidos_autofill()

