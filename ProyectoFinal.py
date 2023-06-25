def cargar_usuarios():
    try:
        with open("usuarios.txt", "r") as archivo:
            usuarios = {}
            for linea in archivo:
                nombre, contrasena = linea.strip().split(",")
                usuarios[nombre] = contrasena
    except FileNotFoundError:
        usuarios = {}
    
    return usuarios

def guardar_usuarios(usuarios):
    with open("usuarios.txt", "w") as archivo:
        for nombre, contrasena in usuarios.items():
            archivo.write(f"{nombre},{contrasena}\n")

def crear_usuario():
    usuarios = cargar_usuarios()
    
    while True:
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        
        if nombre_usuario in usuarios:
            print("El nombre de usuario ya existe. Intente nuevamente.")
        else:
            break
    
    contrasena = input("Ingrese la contraseña: ")
    usuarios[nombre_usuario] = contrasena
    
    guardar_usuarios(usuarios)
    print("Usuario creado exitosamente.")

def iniciar_sesion():
    usuarios = cargar_usuarios()
    
    intentos = 3
    while intentos > 0:
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        
        if nombre_usuario in usuarios:
            contrasena = input("Ingrese su contraseña: ")
            
            if contrasena == usuarios[nombre_usuario]:
                print("Inicio de sesión exitoso.")
                return
            else:
                intentos -= 1
                print(f"Contraseña incorrecta. Le quedan {intentos} intentos.")
        else:
            print("Nombre de usuario no encontrado.")
    
    print("Ha excedido el número de intentos. Inicio de sesión fallido.")

def menu():
    print("== Aplicación de Inicio de Sesión ==")
    print("1. Crear usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    print()

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente nuevamente.")

print("¡Hasta luego!")
