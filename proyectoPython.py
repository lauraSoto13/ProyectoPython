#Variables
basedatos = []
id = 1
baseDatosTemporal = []

class Usuario:
    def __init__(self, id, usuario, password):
        self.id = id
        self.usuario = usuario
        self.password = password

    def modificar(self, usuario, password):
        self.password = password 
        self.nombre = nombre

    def mostrar(self):
        print()
        print(f"El id es; {self.id}, usuario es: {self.usuario}, y la contraseña es: ********" )

def imprimirBd():
    for usuario in basedatos:
            usuario.mostrar()

while True: 
    print("\n Menú")
    print("1. Registro")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Log In")
    print("6. Salir")

    opc = input("Seleccione una opcion")

    if opc == '1':
        nombre = input("Ingrese el nombre del usuario: ")
        password = input("Ingrese la contraseña: ")
        usuario = Usuario(id, nombre, password)
        basedatos.append(usuario)
        id = 1 + int(id)
    elif opc == '2':
        imprimirBd()
        idModificar = input("Ingrese el id del usuario del que desea modificar la contraseña: ")
        nombre = input("Ingrese el nombre del usuario: ")
        password = input("Ingrese la contraseña: ")
        usuarioModificado = Usuario(idModificar, nombre, password)
        for usuario in basedatos:
            if int (idModificar) != (usuario.id):
                baseDatosTemporal.append(usuario)
        basedatos = baseDatosTemporal
        baseDatosTemporal = [ ]
        basedatos.append(usuarioModificado)
        imprimirBd()
    elif opc == '3':
        idEliminar = input("Ingrese el id del usuario a eliminar: ")
        for usuario in basedatos:
            if int (idEliminar) != (usuario.id):
                baseDatosTemporal.append(usuario)
        basedatos = baseDatosTemporal
        baseDatosTemporal = [ ]
        imprimirBd()
    elif opc == '4':
        imprimirBd()
    elif opc == '5':
        usuario_login = input("Ingresar usuario: ")
        password_login = input ("Ingresa la contraseña: ")
        for usuario in basedatos:
            if password_login == usuario.password and usuario_login == usuario.usuario:
                print("Usuario logueado")
                break
            else: 
                print("Credenciales incorrectas")
                break
    elif opc == '6':
        print("Adiós!")
        break
    else: 
        print("Opción no válida!")

