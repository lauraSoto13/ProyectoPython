import pip
pip.main(['install','mysql-connector'])
import mysql.connector 
import hashlib
import subprocess
import sys

def instalar_requierements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "mysql-connector"])
        print("Mysql se instaló correctamente")
    except subprocess.CalledProcessError as e:
        print("Hubo un error al instalar Mysql")

instalar_requierements()

#Variables
id = 1

def hash(dato):
    dato = str(dato)
    return hashlib.sha3_512(dato.encode()).hexdigest()

class Usuario:
    def __init__(self, id, usuario, password, activo):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.activo  = activo 

def imprimirBd():
    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="proyecto")
    cursor1=conexion1.cursor()
    cursor1.execute("select * from usuario where activo = 1")
    for tabla in cursor1:
        print(tabla)
    conexion1.close()


def conectar_bd():
    conexion1=mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="", 
        database="proyecto"
    )
    cursor1=conexion1.cursor()
    return conexion1, cursor1

conexion1, cursor1 = conectar_bd()

while True: 
    palabra = hash("laura") 
    print(palabra)
    print("\n Menú")
    print("1. Registro")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Log In")
    print("6. Salir")

    opc = input("Seleccione una opcion: ")

    if opc == '1':
        nombre = input("Ingrese el nombre del usuario: ")
        password = input("Ingrese la contraseña: ")
        password = hash(password)
        cursor1.execute("insert into usuario (nombre, clave, activo) values (%s,%s, 1)", (nombre, password))
        conexion1.commit()
        id = 1 + int(id)
    elif opc == '2':
        idModificar = input("Ingrese el id del usuario del que desea modificar la contraseña: ")
        nombre = input("Ingrese el nombre del usuario: ")
        password = input("Ingrese la contraseña: ")
        cursor1.execute("update usuario set nombre = %s, clave = %s where id = %s", (nombre, password, idModificar)) 
        conexion1.commit()
        imprimirBd()
    elif opc == '3':
        idEliminar = input("Ingrese el id del usuario a eliminar: ")
        cursor1.execute("update usuario set activo = 0 where id = " + (idEliminar)) 
        conexion1.commit()
        imprimirBd()
    elif opc == '4':
        imprimirBd()
    elif opc == '5':
        usuario_login = input("Ingresar usuario: ")
        password_login = input ("Ingresa la contraseña: ")
        password_login = hash(password_login)
        cursor1.execute("select * from usuario where nombre = %s and clave = %s", (usuario_login, password_login))
        resultado = cursor1.fetchone()
        if resultado:
            print("Usuario logueado")
        else: 
            print("Credenciales incorrectas")
    elif opc == '6':
        print("Adiós!")
        conexion1.close()
        break
    else: 
        print("Opción no válida!")

