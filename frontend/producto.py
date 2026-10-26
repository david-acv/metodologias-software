from tabulate import tabulate
import backend.productos as Producto
from utils.terminal import limpiar

ENCABEZADOS = ["Id", "Nombre", "Precio", "Cantidad"]

def listar_productos():
    productos = Producto.listarProductos()
    print(tabulate(productos, headers=ENCABEZADOS, tablefmt="rounded_grid"))

def consultar_producto():
    id_producto = input("Ingresa el Id del producto: ")
    producto = Producto.consultarProducto(id_producto)
    
    if producto is None:
        print("El producto con Id " + id_producto + " no existe")
        return

    print(tabulate([producto[1:]], headers=ENCABEZADOS, tablefmt="rounded_grid"))

def mostrar_menu_de_productos():
    separador = "-" * 40 
    bienvenida = "Bienvenido a la gestión de productos"

    opciones = {
        "1": listar_productos,
        "2": consultar_producto,
    }

    solicitud = "Ingresa una opción: "
    salida = False

    while True:
        menu = (
            (bienvenida if not salida else separador)
            + "\n1. Listar productos"
            + "\n2. Consultar producto"
            + "\n3. Salir\n"
        )
        print(menu)

        opcion = input(solicitud)
        salida = False

        if opcion == "3":
            limpiar()
            break
        elif opcion in opciones:
            salida = True
            solicitud = "Ingresa una opción: "
            limpiar()
            opciones[opcion]()
        else:
            solicitud = "Opción inválida, ingresa una nueva opción: "
            limpiar()