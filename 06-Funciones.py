# def miFuncion():#si  necesitas valores se pasan aqui y se llaman argumentos
#     ##logica que quiero que ejecute
#     print('Mi primera función')

# ##se tiene que llamar para que se ejecute

# miFuncion()#se les llama parametros lo que se pasa aqui


# #Funciones con parametros y argumentos 

# def imprimeDato(argumento):#argumentos 
#     print('Mi argumento es ' ,argumento)

# imprimeDato('parametro')#parametros


# #funciones con varios argumentos y parametroa

# def nombreCompleto(nombre,apellido):
#     ('El nombre completo es: ' , nombre , ' ' , apellido)


# #Funciones tupla


# def dato(*nombres):#lo recibe como si fuera una variable y no un argumento
#     print(nombres)

# dato('judas','Sebas','Chris')


# #acceder a un solo dato es por el indice


# def dato(*nombres):
#     print(nombres[0])#Imprime solo judas

# dato('judas','Sebas','Chris')


# def nombreCompleto (apellido,nombre):
#     print(nombre,apellido)

# nombre


# alumnosPython=['Judas','Sebas','Christian']
# def alumnos(alumnos):
#     for alumno in alumnos:
#         print(alumno)

# alumnos(alumnosPython)


# #Pasar parametro por referencia

# def materiales(funcionamiento,nombre):
#     print(nombre,funcionamiento)

# materiales(nombre='Pericas', funcionamiento='Apretar')


# #Diccionario

# def animales(**kwargs,):
#     print(kwargs['nombre',kwargs['apellido']]) #con esto sabe que nombre contiene Christian y apellido suarez


# nombreCompleto(nombre='Christan', apellido='Suarez')


# #Argumentos por defecto 

# def miFuncion2(nombre='Spider Man'):
#     print(nombre)

# miFuncion2('Batman')#imprime batman
# miFuncion2()#imprime Spider man 

def mayorDeEdad(edad):
    if edad>18:
        return True
    else:
        return False

def pasarAlBar(siPasa):
    if(True):
        print('Bienvenido')
    else:
        print('No puede pasar')

edad=mayorDeEdad(18)    

pasarAlBar(edad)