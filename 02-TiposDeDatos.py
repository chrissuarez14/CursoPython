#Strings

nombre='Christian' #string
apellido="Suarez" #string

#Enteros

edad=14


#Float o decimal

precio=14.186


#boolean
nombreReal=True
edadReal=False


#Listas
lista=[1,2,3,2]
print(lista)




#Agregar elemento a la lista

print(lista.append(4))#agregar el elemento a la lista el final

#borrar todos los elementos de un arreglo

elementos=lista.clear()
print(elementos)


#contar cuantas veces existe un valor

print(lista.count(2))


#Saber cantidad de elementos

len(lista)


#Borrar el ultimo elemento de un arreglo

mascotas=['Gato','Perro','Pajarito','Cocodrilo','Tigre']


mascotas.pop() #Borrar el ultimo elemento

borrado=mascotas.pop()

print(borrado)

#Borrar un elemento especifico

# mascotas.remove('Tigre')


#Voltear elementos el ultimo al principio

personas=['Christian','Sebas','Judith']

print(personas.reverse())

#Ordenar elementos tiene que ser del mismo tipo

ordenados=personas.sort()

print(ordenados)


######Tupluas


tupla=(1,2,3,4)

print(tupla)

#Saber cuantas veces se repite un elemento 


print(tupla.count(1))

#En que posicion esta un elemento

print(tupla.index(4))


##Range

rango=range(6);

print(rango) # range 0,6


##Diccionarios 


diccionario={
    "nombre":'Christian', #llave:nombre,value o valor:'christian
    "raza":'Persa',
    "edad":5
}

print(diccionario) #ver como lo manda 

#Acceder un elemento

print(diccionario['nombre'])#se accede por la llave

#Mediante metodo

print(diccionario.get('raza'))

diccionario['nombre']='Chente'

print(diccionario)


#cambiar el valor de una propiedad

diccionario['nombre']='Fluffy'

#cantidad de valores del diccionario 

print(len(diccionario))

#Agregar una nueva propiedad

diccionario['ronronea']=True

#Eliminar el ultimo valor del diccionario

diccionario.popitem()

#Eliminar un valor determinado 

diccionario.pop('nombre')

print(diccionario)


#borrar elementos con el metodo "del()" 

del diccionario['raza']
print(diccionario)


#Copiar un diccionario 
mascotasGutierrez={
    "nombre":'Cleopatra',
    "raza":'De la calle',
    "Sonido":'Miau'
}
    
mascotaSebas= mascotasGutierrez.copy()

print(mascotasGutierrez,mascotasGutierrez)

#Eliminar todo el diccionario

mascotaSebas.clear()

print(mascotaSebas)


#Metodo dict para copiar 

diccionario1={
    'nombre':'Suarez',
    'edad':22
}

copiaDiccionario1=dict(diccionario1)

print(copiaDiccionario1)
#Diccionarios anidados

mascotasFamilia={

    'Gato':{
        'nombre':'Cleo',
        'edad':21,
        'color':'Calle'
    },
    'Perro':{
        'nombre':'Niky',
        'edad':21,
        'color':'blanco'
    }    
}


print(mascotasFamilia)

#Otra forma de crear diccionario

gato={
    'nombre':'Venus',
    'edad':21,
    'color':'Calle'
}

perro={
    'nombre':'Scooby',
    'edad':21,
    'color':'Cafe'
}
mascotasChidas={
    'gato':gato,
    'perro':perro
}


#Metodo dict para crear diccioarios

materiales=dict(
    nombre='tijeras',
    uso='cortar'
)

print(materiales)
#acceder a un datos

datoNombre=mascotasFamilia['Gato']
datoN=datoNombre['nombre']
print(datoN)
#metodo dict 


