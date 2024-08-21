saldo = 1000.0  # El saldo inicial en la cuenta
historial = []  # Lista para guardar las transacciones realizadas
PIN = int(1234)

def consultar_saldo():
    """Esta función muestra el saldo actual en la cuenta."""
    global saldo  # Usamos la variable global 'saldo'
    
    print(f"Tu saldo actual es: ${saldo:.2f}")
    
def depositar_dinero():
    """Esta función permite al usuario depositar dinero en su cuenta."""
    global saldo  # Usamos la variable global 'saldo'
    global PIN
    pin = int(input("Ingrese su pin: "))
    if pin == PIN:
        print("")
        cantidad = float(input("Ingresa la cantidad a depositar: $"))
        if cantidad > 0:
            saldo += cantidad
            historial.append(f"Depósito: +${cantidad:.2f}")
            print(f"Has depositado: ${cantidad:.2f}")
        else:
            print("La cantidad a depositar debe ser positiva.")
    else:
        print("PIN incorrecto.")

def retirar_dinero():
    """Esta función permite al usuario retirar dinero de su cuenta."""
    global saldo  # Usamos la variable global 'saldo'
    global PIN
    
    pin = int(input("Ingrese su pin: "))
    
    if pin == PIN:
        print("")
        cantidad = float(input("Ingresa la cantidad a retirar: $"))
        if 0 < cantidad <= saldo:
            saldo -= cantidad
            historial.append(f"Retiro: -${cantidad:.2f}")
            print(f"Has retirado: ${cantidad:.2f}")
        elif cantidad > saldo:
            print("No tienes suficiente saldo para retirar esa cantidad.")
        else:
            print("La cantidad a retirar debe ser positiva.")
    else:
        print("PIN incorrecto.")

def cambiar_pin():
    global PIN
    pin = int(input("Ingrese su PIN: "))
    print("")
    if pin == PIN:
        New_pin = int(input("Ingrese su nuevo PIN: "))
        conf_pin = int(input("Confirme su pin: "))
        if conf_pin == New_pin:
            PIN = New_pin
            print("PIN cambiado con éxito.")
        else:
            print("Error de confirmacion.")
    else:
        print("PIN incorrecto.")         
def ver_historial():
    """Esta función muestra el historial de transacciones realizadas."""
    global PIN
    
    pin = int(input("Ingrese su pin: "))
    
    if pin == PIN:
        if historial:
            print("Historial de transacciones:")
            for transaccion in historial:
                print(transaccion)
        else:
            print("")
            print("No hay transacciones realizadas.")
    else:
        print("PIN incorrecto.")
def menu():
    """Esta función muestra el menú principal y maneja las opciones del usuario."""
    while True:  # Bucle infinito para mostrar el menú hasta que el usuario decida salir
        print("")
        print("-" * 17 ,"Bienvenido al Cajero Automático", "-" * 17)
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Ver Historial de Transacciones")
        print("5. Cambiar PIN")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        print("-" * 67)
        print("")
        
        if opcion == '1':
            consultar_saldo()
        elif opcion == '2':
            depositar_dinero()
        elif opcion == '3':
            retirar_dinero()
        elif opcion == '4':
            ver_historial()
        elif opcion == '5':
            cambiar_pin()
        elif opcion == '6':
            print("Gracias por usar el Cajero Automático. ¡Hasta luego!")
            break  # Salimos del bucle y terminamos el programa
        else:
            print("Opción inválida, por favor elige nuevamente.")

# Llamada directa al menú
menu()  # Iniciamos el sistema de cajero automático