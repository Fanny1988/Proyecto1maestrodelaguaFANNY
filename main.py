# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os

# registro de los estudiantes
listaRegistro = []
matrizA = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
           [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
cont = 0
# contador para manejar la posicion
rango = 10


# funcion para el menu principal
def menuPrincipal():
    # Use a breakpoint in the code line below to debug your script.
    opcionesMenu = [" 1 - Registro de Estudiantes ", " 2 - Lista de Estudiantes ", " 3 - Ingreso de Notas ",
                    " 4 - Lista de Notas", " 5 - Actualizar Nota de estudiante ",
                    " 6 - Clasificacion Aprobados - Reprobados ", " 7 - Salir "]
    limpiarPantalla()
    print("  ****************************************** ")
    print("    MENU PRINCIPAL - REGISTRO DE NOTAS  ")
    print("  ****************************************** ")
    # se imprimen en pantalla las opciones del menu
    for n in opcionesMenu:
        print(n)
    print("  ****************************************** ")
    # se evalua la opcion deseada en el segun
    evaluarOpcion(int(input("  Seleccione una opcion : ")))


# funcion para cada una de las opciones se llama da cada funcion
def evaluarOpcion(opcion):
    if opcion == 1:
        # nediante un if elif condicion se brinda las opciones de menu al usuario
        i = 0
        for i in range(rango):
            limpiarPantalla()
            titulo("  REGISTRO DE ESTUDIANTES")
            registroEstudiantes()
    elif opcion == 2:
        if bool(listaRegistro):
            titulo("     LISTA DE ESTUDIANTES")
            estudiantesRegistrados()  # se llema a la funcion estudianteRegistrados()
            print("  DEBE REALIZAR EL REGISTRO DE ESTUDIANTES PREVIAMENTE ")
        else:
            print("  DEBE REALIZAR EL REGISTRO DE ESTUDIANTES PREVIAMENTE ")
    elif opcion == 3:
        if bool(listaRegistro):
            titulo("     INGRESO DE NOTAS")
            ingresoNotas()  # se llama a la funcion IngressoNotas()
        else:
            print("  DEBE REALIZAR EL REGISTRO DE ESTUDIANTES PREVIAMENTE ")

            def clear():
                os.system("pause")
    elif opcion == 4:
        titulo("     REGISTRO DE NOTAS ACTUAL")
        listaNotas()
    elif opcion == 5:
        titulo("     ACTUALIZACION DE NOTAS")
        actualizarNotas()
    elif opcion == 6:
        titulo("     CIERRE DE CURSO ")
        clasificacion("Estudiantes aprobados", 1)
        clasificacion("Estudiantes reprobados", 2)
    elif opcion == 7:
        titulo("     MUCHAS GRACIAS... ")
        exit()
    input("Presione una tecla para continuar...")


def limpiarPantalla():
    os.system("cls")


# recibe por parametro un mensaje que se imprime, de manera unica depende de la funcion
def titulo(mensaje):
    print("  ****************************************** ")
    print(f" {mensaje}  ")
    print("  ****************************************** ")


# definicion del objeto y las propiedades
class persona:
    def __init__(self, id, nombre, seccion):
        self.id = id
        self.nombre = nombre
        self.seccion = seccion


# funcionpara el registro de un objeto de tipo persona
def registroEstudiantes():
    id = int(input("Ingrese la identificacion : "))
    nombre = input("Ingrese el nombre         : ")
    seccion = input("Ingrese la seccion        : ")
    alumno = persona(id, nombre, seccion)  # objeto de tipo alumno
    listaRegistro.append(alumno)  # se agrega el alumno al vector


def ingresoNotas():
    # si se tienen estudiantes se registran las notas
    print(" INGRESO DE NOTAS MATERIAS BASICAS")
    # se itera sobre la lista de personas
    indice = 0
    for n in listaRegistro:
        persona = n
        seccion = persona.seccion
        nombre = persona.nombre
        print(f"Ingreso de notas para {nombre} de la seccion {seccion}")
        ciencias = int(input("Ingrese la nota de Ciencias : "))
        espanol = int(input("Ingrese la nota de Español : "))
        matematica = int(input("Ingrese la nota de Estudios Sociales : "))
        estudiosS = int(input("Ingrese la nota de Matematica : "))
        # se agrega en la posicion la persona
        matrizA[indice] = [ciencias, espanol, matematica, estudiosS]
        indice = indice + 1


def estudiantesRegistrados():
    for n in listaRegistro:
        persona = n
        print(f" NOMBRE DEL ESTUDIANTE :\t {persona.nombre} SECCION DEL ESTUDIANTE :\t {persona.seccion} ")


def actualizarNotas():
    idBuscar = int(input("Ingrese la identificacion del estudiante : "))
    contInterno = 0
    # se itera la lista hasta encontrar el id deseado
    for n in listaRegistro:
        # se recibe el objeto persona
        persona = n
        id = persona.id
        # si el id coincide se actualizan los elementos
        if id == idBuscar:
            ciencias = int(input("Ingrese la nota de Ciencias : "))
            espanol = int(input("Ingrese la nota de Español : "))
            matematica = int(input("Ingrese la nota de Estudios Sociales : "))
            estudiosS = int(input("Ingrese la nota de Matematica : "))
            matrizA[contInterno] = [ciencias, espanol, matematica, estudiosS]
        contInterno = contInterno + 1


# se muestran las notas en general
def listaNotas():
    indice = 0
    for n in listaRegistro:
        persona = n
        # se muestra la informacion detallada de la persona
        print(f" NOTAS DE : {persona.nombre} de la seccion {persona.seccion} : {matrizA[indice]}")
        indice = indice + 1


# se imprime si la persona aprobo o no. opcion indica que debe de mostrar se llama al metodo dos veces
# uno para cada caso
def clasificacion(tipo, opcion):
    print("  ****************************************** ")
    print(f"\n Listado de {tipo}")
    print("  ****************************************** ")
    indiceMatriz = 0
    for n in listaRegistro:
        promedio = (matrizA[indiceMatriz][0] + matrizA[indiceMatriz][1] + matrizA[indiceMatriz][2] +
                    matrizA[indiceMatriz][3]) / 4
        persona = n
        seccion = persona.seccion
        nombre = persona.nombre
        if opcion == 1:
            if promedio >= 65:
                print(f"El estudiante {nombre} de la seccion {seccion} tiene el siguiente promedio : {promedio}")
                print("Porcentaje por materia :")
                informacion(indiceMatriz)
        if opcion == 2:
            if promedio < 65:
                print(f"El estudiante {nombre} de la seccion {seccion} tiene el siguiente promedio : {promedio}")
                print("Porcentaje por materia :")
                informacion(indiceMatriz)

        indiceMatriz = indiceMatriz + 1


# informacion del valor porcentual de las notas
def informacion(indiceMatriz):
    print(
        f" Para la materia de Español obtuvo nota de {matrizA[indiceMatriz][0]} lo cual es {matrizA[indiceMatriz][0] * (25 / 100)}/25")
    print(
        f" Para la materia de Matematicas obtuvo nota de {matrizA[indiceMatriz][1]} lo cual es {matrizA[indiceMatriz][1] * (25 / 100)}/25")
    print(
        f" Para la materia de Estudios Sociales obtuvo nota de {matrizA[indiceMatriz][2]} lo cual es {matrizA[indiceMatriz][2] * (25 / 100)}/25")
    print(
        f" Para la materia de Ciencias obtuvo nota de {matrizA[indiceMatriz][3]} lo cual es {matrizA[indiceMatriz][3] * (25 / 100)}/25")


# llamado del main
if __name__ == '__main__':
    while True:
        menuPrincipal()


