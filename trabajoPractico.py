# # Función para saber si no hay ningun trabajador.

def sinTrabajadores(trabajadores):
    if len(trabajadores) == 0:
        a = input("No hay trabajadores registrados actualmente. ¿Desea agregar alguno? (S/N):").upper()
        while a != "S" and a != "N":
            a = input("Error. Por favor ponga S/N si quiere agregar trabajador").upper()
        if a == "S":
            agregar(trabajadores)
        elif a == "N":
            print("-"*50)
            print("Okay volvemos al menu de reportes entonces.")
            return

estado = bool   # Para saber si el usuario se encuentra en la empresa

# Función para ingresar un nuevo trabajador.
def agregar(trabajador):
    while True:
        dni = input("Ingrese el DNI del trabajador (debe tener entre 3 y 8 dígitos):\n")
        if len(dni) in range(3, 9):
            try:
                dni = int(dni)
                break
            except ValueError:
                print("El DNI debe ser un número. Ingrese nuevamente.")
        else:
            print("El DNI debe tener entre 3 y 8 dígitos. Ingrese nuevamente.")


    while dni in trabajador:
        dni = int(input("¡Ya existe! Ingrese otro dni para agregar:\n"))
    nombre = input("Ingrese el nombre y apellido del trabajador para agregar:\n").title()
    while True:
        try:
            edad = int(input("Ingrese la edad del trabajador:\n"))
            break
        except:
            print("La edad tiene que ser un numero, por favor ingrese nuevamente su edad:")
    while edad not in range(18, 66):
        edad = int(input("El trabajador no puede ser menor a 18 años, ni mayor a 65 años. Ingrese nuevamente la edad del trabajador:\n"))
    profesion = input("Ingrese la profesión del trabajador:\n").capitalize()
    descripcion = input ("Ingrese una descripción corta (máx. 50 caracteres):\n").capitalize()
    while len(descripcion) > 50:
        descripcion = input ("Límite de caracteres excedido. Ingrese nuevamente una descripción corta:\n").capitalize()
    
    estado = input("¿El trabajador está activo en la empresa? (S/N):\n").upper()
    while estado != "S" and estado != "N":
        estado = input("Error. Por favor ingrese si el trabajador está activo en la empresa con (S/N):\n").upper()
    if estado == "S":
        estado = True
    else:
        estado = False
    trabajador [dni] = [nombre, edad, profesion, descripcion, estado]

# Función para modificar los dato ingresados del trabajador existente.
def modificar(cuentas):
    sinTrabajadores(cuentas)
    if len(cuentas)>0:

        while True:
            try:
                dni = int(input("Ingrese el DNI del trabajador:\n"))
                break
            except ValueError:
                print("El DNI debe ser un número. Por favor, ingrese nuevamente.")

        while dni not in cuentas:
            dni = int(input("¡No existe el DNI ingresado! Ingrese un DNI existente ('0' para volver atrás):\n"))
            if dni == 0:
                menu_gestion_trabajadores()
            
        
        opcion = int(input('''
        Ingrese la opción que desea modificar:
        1- DNI
        2- Nombre y Apellido
        3- Edad
        4- Profesión
        5- Descripción
        6- Estado
        '''))
        while True:
            if opcion <= 6 and opcion >= 1:
                match opcion:
                    case 1:  # DNI (clave)
                        while True:
                            try:
                                nuevo_dni = int(input(f"Ingrese el nuevo DNI del trabajador para {cuentas[dni][0]}:\n"))
                                break
                            except ValueError:
                                print("El nuevo DNI debe contener solo números. Por favor, ingrese nuevamente:")
                        while nuevo_dni in cuentas:
                            nuevo_dni = int(input(f"¡El DNI ya existe! Ingrese un nuevo DNI para el trabajador {cuentas[dni][0]}:\n"))
                        cuentas[nuevo_dni] = cuentas[dni]
                        cuentas.pop(dni)
                        print("-" * 50)
                        print("¡Se modificó el DNI exitosamente!")
                        print("-" * 50)
                        break

                    case 2:  
                        nombre = input(f"Ingrese el nuevo nombre y apellido del trabajador {cuentas[dni][0]}:\n").capitalize()
                        cuentas[dni][0] = nombre
                        print("-" * 50)
                        print("¡Se modificó el nombre y apellido exitosamente!")
                        print("-" * 50)
                        break

                    case 3:  
                        while True:
                            try:
                                edad = int(input(f"Ingrese la nueva edad del trabajador {cuentas[dni][0]}:\n"))
                                break
                            except ValueError:
                                print("La edad debe ser un número. Por favor, ingrese nuevamente:")
                        while edad not in range(18, 66):
                            edad = int(input("La persona no puede ser ni menor a 18 años, ni mayor a 65 años. Ingrese nuevamente la edad del trabajador:\n"))
                        cuentas[dni][1] = edad
                        print("-" * 50)
                        print("¡Se modificó la edad exitosamente!")
                        print("-" * 50)
                        break

                    case 4:  
                        profesion = input(f"Ingrese la nueva profesión del trabajador {cuentas[dni][0]}:\n").capitalize()
                        cuentas[dni][2] = profesion
                        print("-" * 50)
                        print("¡Se modificó la profesión exitosamente!")
                        print("-" * 50)
                        break

                    case 5:  
                        descripcion = input("Ingrese una nueva descripción corta (máx. 50 caracteres):\n").capitalize()
                        while len(descripcion) > 50:
                            descripcion = input("Límite de caracteres excedido. Ingrese nuevamente una descripción corta:\n").capitalize()
                        cuentas[dni][3] = descripcion
                        print("-" * 50)
                        print("¡Se modificó la descripción exitosamente!")
                        print("-" * 50)
                        break

                    case 6:  
                        estado = input(f"¿El trabajador {cuentas[dni][0]} está activo en la empresa? (S/N):\n").lower()
                        cuentas[dni][4] = estado
                        print("-" * 50)
                        print("¡Se modificó el estado exitosamente!")
                        print("-" * 50)
                        break


            opcion = int(input("Opción no válida. Ingrese nuevamente:"))

# Función para eliminar un trabajador existente.
def eliminar(informacion):
    sinTrabajadores(informacion)
    if len(informacion)>0:
        while True:
            try:
                dni_trabajador = int(input("Ingrese el DNI del trabajador que desea eliminar:\n"))
                break
            except:
                print("El DNI solo debe contener números.")
        while dni_trabajador not in diccionario:
            dni_trabajador = input("¡No existe! Ingrese nuevamente el DNI del trabajador que desea eliminar ('0'Para volver atrás):\n")
            if dni_trabajador == "0":
                menu_principal()
            else:
                print("Opción inválida. Por favor, ingrese una opción válida:\n")

        seguridad = input("¿Está seguro que desea eliminarlo? (Presione 's' para continuar. (Con otra letra se cancela)):\n ").lower()
        if seguridad == "s":
            informacion.pop(dni_trabajador)
            print("¡Se eliminó a existosamente!\n")
        else:
            print("Usted ha cancelado la operación.\n")

# Función para ver la información de un trabajador según su DNI.
def mostrar_informacion(trabajadores):
    sinTrabajadores(trabajadores)
    if len(trabajadores)>0:
    
        while True:
            try:
                dni = int(input("Ingrese el DNI del trabajador que desea ver:\n"))
                break
            except ValueError:
                print("El DNI solo puede ser números. Por favor ingrese nuevamente:\n")
        
        if dni in trabajadores:
            print(f'''Información:
                Trabajador: {trabajadores[dni][0]}
                Edad: {trabajadores[dni][1]}
                Profesión: {trabajadores[dni][2]}
                Descripción: {trabajadores[dni][3]}
                ''',end=(""))
            if trabajadores[dni][4] == True:
                print("Estado: Si se encuentra activo en la empresa")
            elif trabajadores[dni][4] == False:
                print("Estado: El trabajador no se encuentra activo en la empresa")
        else:
            print("No existe el DNI ingresado. Ingrese un DNI existente para ver.")

# Función para mostrar los trabajadores desocupados (no activos).

def mostrar_desocupados(trabajadores):
    sinTrabajadores(trabajadores)

    if len(trabajadores)>0:

        while True:
            try:
                dni = int(input("Ingrese el DNI del trabajador desocupado que desea ver:\n"))
                break
            except ValueError:
                print("El DNI solo puede ser números. Por favor ingrese nuevamente:\n")
        while dni not in trabajadores:
            dni = int(input("El DNI no existe. Por favor ingrese un DNI existente.\n"))
        if dni in  trabajadores and trabajadores[dni][4] == False:
            print(f'''Información:
                Trabajador: {trabajadores[dni][0]}
                Edad: {trabajadores[dni][1]}
                Profesión: {trabajadores[dni][2]}
                Descripción: {trabajadores[dni][3]}
                Estado: Inactivo
                ''')
            print("-"*50)
            
            
        elif trabajadores[dni][4] == True:
            print(f'''Información:
                Trabajador: {trabajadores[dni][0]}
                Edad: {trabajadores[dni][1]}
                Profesión: {trabajadores[dni][2]}
                Descripción: {trabajadores[dni][3]}
                Estado: Se encuentra trabajando en la empresa.
                ''')
            print("-"*50)
        else:
            print("No existe el DNI ingresado. Ingrese un DNI existente para ver.")

# Función para mostrar los trabajadores según la profesión indicada.
def mostrar_profesion(diccionario):
    profesion = input("Ingrese la profesión que desea ver: ").capitalize()
    print("-"*50)
    
    while profesion not in [valores[2] for valores in diccionario.values()]:
        print("No existe la profesión ingresada. Intente nuevamente ('0' para volver atrás)")
        profesion = input("Ingrese la profesión que desea ver: ").capitalize()
        print("-"*50)
        if profesion == "0":
            return
    
    for dni, valores in diccionario.items():
        if valores[2] == profesion:
            print(f"DNI: {dni}")
            print(f"Nombre: {valores[0]}")
            print(f"Edad: {valores[1]}")
            print(f"Profesión: {valores[2]}")
            print("-" * 50)

# Diccionario vacio para almacenar los  trabajadores.
diccionario = {}


def menu_principal():
    while True:
        print("-"*50)
        print("\n--- Menú Principal ---")
        print("[A] Gestión de Trabajadores")
        print("[B] Reportes")
        print("[C] Salir")
        opcion = input("Ingrese la opción deseada: ").lower()
        print("-"*50)            
        if opcion == "a":
            menu_gestion_trabajadores()
        elif opcion == "b":
            menu_reportes()
        elif opcion == "c":
            print("-"*50)
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Menú de gestión de trabajadores.
def menu_gestion_trabajadores():
    while True:
        print("\n--- Menú de Gestión de Trabajadores ---")
        print("[1] Ingresar nuevo Trabajador")
        print("[2] Modificar dato de trabajador")
        print("[3] Eliminar Trabajador")
        print("[4] Volver")
        opcion = input("Ingrese la opción deseada: "+"\n" )
        # print("\n")
        print("-"*50)

        if opcion == "1":
            agregar(diccionario)
        elif opcion == "2":
            modificar(diccionario)
        elif opcion == "3":
            eliminar(diccionario)
        elif opcion == "4":
            break  
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Menú de reportes.
def menu_reportes():
    while True:
        print("\n--- Menú de Reportes ---")
        print("[1] Ver la información de un trabajador según su DNI")
        print("[2] Mostrar trabajadores desocupados (no activos)")
        print("[3] Mostrar trabajadores según la profesión")
        print("[4] Volver")
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            mostrar_informacion(diccionario)
        elif opcion == "2":
            mostrar_desocupados(diccionario)
        elif opcion == "3":
            mostrar_profesion(diccionario)
        elif opcion == "4":
            return
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Función principal para iniciar el programa.
def iniciar_programa():
    menu_principal()

# Inicio del programa.
iniciar_programa()
if diccionario == {}:
    print("No hay ningun dato algún trabajador que mostrar.\n")
else:
    print("Todas las cuentas de los trabajadores registrados:\n")
    for x,i in diccionario.items():
        print(f'''
        ------------------------------------------
        DNI: {x}
        Nombre: {i[0]}
        Edad: {i[1]}
        Profesion: {i[2]}
        Descripcion: {i[3]}
        ''', end=(""))
        if i[4] == True:
            print("Estado: Activo en la empresa.\n")
        elif i[4] == False:
            print("Estado: No está activo en la empresa.\n")
print("*"*50)
print("                  ¡Hasta luego!")
print("*"*50)