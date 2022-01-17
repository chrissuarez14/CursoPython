#########Loops

#se repite hasta que se cumpla una condicion de salida

i=0

while i<5:
    print('el valor es ' ,i)
    i+=1 #i=i+1 suma el valor de i en 1 

##Si queremos detener la ejecucion del while  podemos usar break 

while i<5:
    print('el valor es ' ,i)
    if i==3:
        break #aqui se van  imprimir los valores de 0 a 3 y luego se detiene 
    i+=1

##Si queremos continuar el loop se va a saltar todo lo que esta debajo de nuestro loop  y vuelve a checar 

while i<5:

    print('el valor es ' ,i)
    if i==3:
        continue
    i+=1# Este se lo soltara y causara el rproblema de que se vuelva infinito llega a 3 a y luego 3 3 3 y asi siempre


##Para solucionarlo 

while i<5:
    i+=1
    if i==3:
        continue
    print('el valor es ' ,i) #aqui imprimira del 1 al 5 saltando el 3



#Se usa cuando queramos iterar listas o tuplas pero generalmente son datos tambien podemos iterar diccionarios


usuarios=['Christian','Sebas','Judas']

for usuario in usuarios:#la x o lo que va a en la x es como le quiero llamar a cad uno de estos datos 
    print(usuario)


#Podemos iterar sobre strings

usuario='Judith'

for caracter in usuario:
    print(caracter)#imprimira judith 

#Tambien podemos usar la palabra break

alumnos=['Judith','Christian','Sebas','Cleo']

for caracter in alumnos:
    if caracter=='Sebas':
        break
    print(usuario)



#Continue se salta el caracter en este caso y sigue 
for caracter in alumnos:
    if caracter=='Sebas':
        continue
    print(usuario) #judith christian cleo 



#usar range 
for x in range(6):
    print(x)#0 al 6

#usar range indicando por el valor que inicia

for x in range(1,6):
    print(x)#del 1 al 5

#con un 3 parametro indicara que cuando aumente vaya aumentando de 1 en 1 o 2 en 2


for x in range(3,30,5):
    print(x)# 3 8 13 15 23 28


#En los loops for podemos usar el else y este se usa cuando ya haya terminado de iterar todos los elementos

for x in range(1,50):
    print(x)
else:
    print('Hemos terminado')


#for dentro de for por lo regular no es buena idea pero por uso practico

personas=['Judith','Sebas ','Christian','Estefanía']
mascotas=['Baxter','Venus','Patrick','Cleo']

for persona in personas:
    for mascota in mascotas:
        print('La persona ' , persona , ' tiene de mascota a ', mascota)

