#Nombre: Miqueas Servettin
#div 316
#legajo:112979

def cargar_productos(): 
    # Pregunta al usuario cuántos productos desea ingresar
    n = int(input("¿Cuántos productos deseas ingresar? "))
    # Crea una lista vacía con espacio para n productos
    inventario = [None] * n  
    # Recorre del 0 a n-1 para ingresar los datos de cada producto
    for i in range(n):
        nombre = input(f"Nombre del producto {i + 1}: ")   # Nombre del producto
        precio = float(input("Precio del producto: "))    # Precio del producto
        cantidad = int(input("Cantidad del producto: "))  # Cantidad disponible
        # Guarda los datos en la posición i de la lista inventario
        inventario[i] = [nombre, precio, cantidad]
    # Retorna la lista completa con los productos cargados
    return inventario

def buscar_producto(inventario):
    # Solicita el nombre del producto a buscar
    nombre_buscar = input("Nombre del producto a buscar: ")
    # Recorre cada producto dentro del inventario
    for producto in inventario:
        # Compara si el nombre del producto coincide con el buscado
        if producto[0] == nombre_buscar:
            # Muestra la información del producto encontrado
            print("\n--- Producto encontrado ---")
            print(f"Nombre  : {producto[0]}")
            print(f"Precio  : {producto[1]}")
            print(f"Cantidad: {producto[2]}")
            return  # Sale de la función luego de encontrar el producto
    # Si no encontró ningún producto con ese nombre, informa al usuario
    print("Producto no encontrado.")

def ordenar_inventario(inventario):
    # Verifica si el inventario está vacío
    if not inventario:
        print("No hay productos cargados.")
        return
    # Algoritmo de ordenamiento burbuja para ordenar por precio de menor a mayor
    n = len(inventario)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara precios de productos adyacentes
            if inventario[j][1] > inventario[j + 1][1]:  # Si el actual es más caro que el siguiente
                # Intercambia las posiciones para ordenar
                inventario[j], inventario[j + 1] = inventario[j + 1], inventario[j]

    # Imprime el inventario ordenado
    print("Inventario ordenado por precio:")
    for producto in inventario:
        print(f"Nombre  : {producto[0]}")
        print(f"Precio  : {producto[1]}")
        print(f"Cantidad: {producto[2]}")
        print("------------------------")

def mostrar_mas_caro(inventario):
    # Verifica que el inventario no esté vacío
    if not inventario:
        print("No hay productos cargados.")
        return

    # Inicializa el producto más caro con el primer elemento
    mas_caro = inventario[0]

    # Recorre la lista para encontrar el producto con mayor precio
    for i in range(1, len(inventario)):
        if inventario[i][1] > mas_caro[1]:
            mas_caro = inventario[i]

    # Muestra el producto más caro encontrado
    print("Producto más caro:")
    print(f"Nombre  : {mas_caro[0]}")
    print(f"Precio  : {mas_caro[1]}")
    print(f"Cantidad: {mas_caro[2]}")

def mostrar_mas_barato(inventario):
    # Verifica que el inventario no esté vacío
    if not inventario:
        print("No hay productos cargados.")
        return

    # Inicializa el producto más barato con el primer elemento
    mas_barato = inventario[0]

    # Recorre la lista para encontrar el producto con menor precio
    for i in range(1, len(inventario)):
        if inventario[i][1] < mas_barato[1]:
            mas_barato = inventario[i]

    # Muestra el producto más barato encontrado
    print("Producto más barato:")
    print(f"Nombre  : {mas_barato[0]}")
    print(f"Precio  : {mas_barato[1]}")
    print(f"Cantidad: {mas_barato[2]}")

def menu():
    # Inicializa inventario vacío para almacenar productos
    inventario = []
    while True:
        # Muestra las opciones del menú principal
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Cargar producto/s")
        print("2. Buscar producto")
        print("3. Ordenar inventario")
        print("4. Mostrar producto más caro")
        print("5. Mostrar producto más barato")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        # Ejecuta la acción según la opción elegida
        if opcion == '1':
            inventario = cargar_productos()          # Carga nuevos productos
        elif opcion == '2':
            buscar_producto(inventario)              # Busca producto por nombre
        elif opcion == '3':
            ordenar_inventario(inventario)           # Ordena inventario por precio
        elif opcion == '4':
            mostrar_mas_caro(inventario)             # Muestra el producto más caro
        elif opcion == '5':
            mostrar_mas_barato(inventario)           # Muestra el producto más barato
        elif opcion == '6':
            print("Saliendo del sistema...")          # Mensaje de salida
            break                                    # Termina el ciclo y el programa
        else:
            # Si se ingresa una opción inválida
            print("Opción inválida. Intenta nuevamente.")

# Llama a la función menu para iniciar el programa
menu()
