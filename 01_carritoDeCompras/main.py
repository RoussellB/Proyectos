from datetime import datetime

# Catalogo de los productos
catalogo = {
    "A001": {"nombre": "Pan", "precio": 1.50},
    "B203": {"nombre": "Leche", "precio": 3.80},
    "C150": {"nombre": "Huevos", "precio": 6.00},
    "D010": {"nombre": "Arroz", "precio": 2.90},
    "E321": {"nombre": "Azúcar", "precio": 2.50},
    "F555": {"nombre": "Café", "precio": 7.20},
    "G777": {"nombre": "Aceite", "precio": 8.90},
    "H888": {"nombre": "Sal", "precio": 1.20},
    "I999": {"nombre": "Fideos", "precio": 3.40},
    "J111": {"nombre": "Galletas", "precio": 4.50},
}

carrito = {}

# Funcion para mostrar el catalogo
def mostrar_catalogo():
    print("Catálogo:")
    for codigo, producto in catalogo.items():
        print(f"Código: {codigo} | Producto: {producto['nombre']} | Precio: S/{producto['precio']:.2f}")

# Funcion para poder agragar los productos
def agregar_producto():
    codigo = input("Ingrese código de producto: ").upper()
    if codigo in catalogo:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("Cantidad inválida.")
                return
            carrito[codigo] = carrito.get(codigo, 0) + cantidad
            print("Producto agregado al carrito.")
        except ValueError:
            print("Cantidad no válida.")
    else:
        print("Código de producto no encontrado.")

# Funcion para eliminar productos
def eliminar_producto():
    codigo = input("Ingrese código de producto a eliminar: ").upper()
    if codigo in carrito:
        del carrito[codigo]
        print("Producto eliminado del carrito.")
    else:
        print("Producto no está en el carrito.")

# Funcion para vacia el carrito
def vaciar_carrito():
    carrito.clear()
    print("Carrito vaciado.")

# Funcion para mostrar el los productos agregados
def mostrar_carrito():
    if not carrito:
        print("Tu carrito está vacío.")
        return
    print("Tu carrito:")
    total = 0
    for codigo, cantidad in carrito.items():
        nombre = catalogo[codigo]["nombre"]
        precio = catalogo[codigo]["precio"]
        subtotal = precio * cantidad
        total += subtotal
        print(f"- {nombre} (x{cantidad}) -> S/{subtotal:.2f}")
    print(f"Total: S/{total:.2f}")

# Funcion finalizar compra
def finalizar_compra():
    if not carrito:
        print("No hay productos en el carrito para comprar.")
        return

    print("Resumen de compra:")
    total = 0
    for codigo, cantidad in carrito.items():
        nombre = catalogo[codigo]["nombre"]
        precio = catalogo[codigo]["precio"]
        subtotal = precio * cantidad
        total += subtotal
        print(f"{nombre} (x{cantidad}) -> S/{subtotal:.2f}")

    print(f"Total a pagar: S/{total:.2f}")
    print("Gracias por tu compra")

    carrito.clear()

# Funcion principal para el menu
def tiendaVirtual():
    while True:
        print("Bienvenido a la tienda virtual")
        print("¿Qué deseas hacer?")
        print("1. Ver catálogo")
        print("2. Agregar producto al carrito")
        print("3. Eliminar producto del carrito")
        print("4. Vaciar carrito")
        print("5. Mostrar carrito")
        print("6. Finalizar compra")
        print("7. Salir")
        opcion = input("> ")

        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            vaciar_carrito()
        elif opcion == "5":
            mostrar_carrito()
        elif opcion == "6":
            finalizar_compra()
        elif opcion == "7":
            print("Byes")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecutar tienda virtual
tiendaVirtual()
