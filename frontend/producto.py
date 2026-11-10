from tabulate import tabulate
import backend.productos as Producto
from utils.terminal import limpiar

ENCABEZADOS = ["Id", "Nombre", "Precio", "Cantidad"]

def pedirNumero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            numero = float(texto)
        except ValueError:
            print("Debes ingresar un número, intenta de nuevo")
            continue
        return int(numero) if numero.is_integer() else numero

def solicitarProducto():
    id_producto = input("Ingresa el Id del producto: ")
    nombre = input("Ingresa el nombre del producto: ")
    precio = pedirNumero("Ingresa el precio del producto: ")
    cantidad = pedirNumero("Ingresa la cantidad del producto: ")
    return (id_producto, nombre, precio, cantidad)

def listarProductos():
    productos = Producto.listarProductos()
    print(tabulate(productos, headers=ENCABEZADOS, tablefmt="rounded_grid"))

def consultarProducto():
    id_producto = input("Ingresa el Id del producto: ")
    producto = Producto.consultarProducto(id_producto)
    if producto is None:
        print("El producto con Id " + id_producto + " no existe")
        return
    print(tabulate([producto[1:]], headers=ENCABEZADOS, tablefmt="rounded_grid"))

def crearProducto():
    nuevo_producto = solicitarProducto()
    producto_creado = Producto.crearProducto(*nuevo_producto)
    if producto_creado:
        print("Producto agregado exitosamente")
    else:
        print("Error agregando el producto, verifique que el Id no exista ya")

def eliminarProducto():
    id_producto = input("Ingresa el Id del producto a eliminar: ")
    producto_eliminado = Producto.eliminarProducto(id_producto)
    if producto_eliminado:
        print("Producto eliminado exitosamente")
    else:
        print("Error eliminando el producto, verifique que el producto con ese Id sí existe")

def actualizarProducto():
    nuevo_producto = solicitarProducto()
    producto_actualizado = Producto.actualizarProducto(*nuevo_producto)
    if producto_actualizado:
        print("Producto actualizado exitosamente")
    else:
        print("Error actualizando el producto, verifique que el producto con ese Id sí existe")

def mostrar_menu_de_productos():
    separador = "-" * 40
    bienvenida = "Bienvenido a la gestión de productos"

    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
        "3": crearProducto,
        "4": eliminarProducto,
        "5": actualizarProducto
    }

    solicitud = "Ingresa una opción: "
    salida = False

    while True:
        menu = (
            (bienvenida if not salida else separador)
            + "\n1. Listar productos"
            + "\n2. Consultar producto"
            + "\n3. Agregar producto"
            + "\n4. Eliminar producto"
            + "\n5. Actualizar producto"
            + "\n6. Salir\n"
        )
        print(menu)

        opcion = input(solicitud)
        salida = False

        if opcion == "6":
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