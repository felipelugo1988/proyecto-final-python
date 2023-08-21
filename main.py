#Primer avance del poryecto aqui creamos una funcion

def mostrar_menu():
    print("Menú:")
    print("a. Pedidos")
    print("b. Clientes")
    print("c. Menú")
    print("d. Salir")

def opcion_pedidos():
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))
    unidades = int(input("Ingrese el número de unidades a solicitar: "))
    
    costo_total = precio_producto * unidades
    print(f"Costo total para {unidades} unidades de {nombre_producto}: ${costo_total:.2f}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").lower()
        
        if opcion == 'a':
            opcion_pedidos()
        elif opcion == 'b':
            print("Opción Clientes seleccionada.")
        elif opcion == 'c':
            print("Opción Menú seleccionada.")
        elif opcion == 'd':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
