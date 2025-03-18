#las librerías que necesito para que mi programa se ejecute correctamente y haga el ambiente virtual.
import pip
pip.main(['install','mysql-connector'])
import mysql.connector 
import hashlib
import subprocess
import sys

#Función que instala mysql-connector con ayuda de pip, además de que 
#   va a manejar los posibles errores con ayuda del try-except.
def instalar_requierements():
    try:
        #Ejecutará el comando en la terminal
        subprocess.check_call([sys.executable, "-m", "pip", "install", "mysql-connector"])
        #Mandará un mensaje que indique si se instaló correctamente.
        # sys.executable = Obtendrá la ruta del ejecutable de oPython
        # -m = Se ejecutará como script
        # pip = Administrador de paquetes de Python
        # install = Comando de pip que dará pie a la instalación
        # mysql-connector = El pquete que se querrá instalar.
        print("Mysql se instaló correctamente")
    #En caso de que falle la instalación, se va a arrojar 
    #   una excepción de tipo subprocesss.CalledProcessError.
    except subprocess.CalledProcessError as e:
        #Mandará un mensaje de aviso.
        print("Hubo un error al instalar Mysql")

#Se manda llamar la función que hemos creado anteriormente para que se ejecute.
instalar_requierements()

#Variables
#Variable patra guardar el id, inicializado en 1 para que en este número comience.  
id = 1

#Función hash que me permitirá pasar la contrasela visible a un hash. 
def hash(dato):
    dato = str(dato)
    return hashlib.sha3_512(dato.encode()).hexdigest()

class Usuario:
    def __init__(self, id, usuario, password, activo):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.activo  = activo 

#Esta fución va a conectar a la base de datos, hace la consulta y la podrá imprimir donde la llamemos.
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

#Función que me permitirá conectarme con la base de datos. 
def conectar_bd():
    conexion1=mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="", 
        database="proyecto"
    )
    cursor1=conexion1.cursor()
    return conexion1, cursor1

#Se manda a llama la función. 
conexion1, cursor1 = conectar_bd()

#Inicio del menú. 
while True:
    print(palabra)
    print("\n Menú")
    print("1. Registro de usuario.")
    print("2. Modificar usuario.")
    print("3. Eliminar usuario.")
    print("4. Mostrar usuarios.")
    print("5. Log In de usuario.")
    print("6. Salir")

    opc = input("Seleccione una opcion: ")

    #Registro de usuarios.
    if opc == '1':
        nombre = input("Ingrese el nombre del usuario: ")
        password = input("Ingrese la contraseña: ")
        password = hash(password)
        cursor1.execute("insert into usuario (nombre, clave, activo) values (%s,%s, 1)", (nombre, password))
        #Me confirmará la transacción a la base de datos.
        conexion1.commit()
        #Actualiza el valor del id para los usuarios registrados.
        id = 1 + int(id)

    #Modificar datos del usuario.
    elif opc == '2':
        idModificar = input("Ingrese el id del usuario del que desea modificar la contraseña: ")
        nombre = input("Ingrese el nombre del usuario: ")
        password = input("Ingrese la contraseña: ")
        cursor1.execute("update usuario set nombre = %s, clave = %s where id = %s", (nombre, password, idModificar)) 
        conexion1.commit()
        imprimirBd()

    #Eliminar usuario. 
    elif opc == '3':
        idEliminar = input("Ingrese el id del usuario a eliminar: ")
        cursor1.execute("update usuario set activo = 0 where id = " + (idEliminar)) 
        conexion1.commit()
        imprimirBd()

    #Mostrar usuarios. 
    elif opc == '4':
        imprimirBd()
    
    #Log-In del usuario.
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
    
    #Salir.
    elif opc == '6':
        print("Adiós!")
        conexion1.close()
        break

    #El usuario eligió una opción incorrecta.
    else: 
        print("Opción no válida!")

