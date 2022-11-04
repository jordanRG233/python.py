#variable=""
#v_1=input("introduce el texto")
#if v_1==variable:
 # print("has logrado tu cometido")
#else:
 #   print("no se pudo lograr")

#v_1=1,2,3,4,5
#print(v_1,end="")
#print("6")
#print("a","b","c","d","e",sep="")
#print("a","b","c","d","e",end= " f ")
#v_1=int(input("ingresa el numero "))
#while v_1<=10 and v_1!=0 and v_1<=0 :
  #print("el resultado es menor o es igual a 10 ")
  #break
#else:
    #print("el resultado esta por encima de 10 ")
#v_1="hola maria "
#c=v_1.count("a")
#print(c)
#print(v_1,type(v_1))
#print("vamos a jugar")
#v_1=int(input(" escribe un numero  "))
#while 20>=v_1>=10 :
     # print("el numero esta entre 10 y 20 ")
     # v_1=int(input("dame otro numero"))
      
#else:
 # print("el numero esta o bien por debajo de 10 o por encima de 20")
#v="s"
#while v=="s":
#  print("seguimos jugando")
#  v=input("quieres seguir jugando s/n")
#print("el juego se ha detenido")
#numero=3
#cont=1
#usuario=int(input("escribe un numero del 1 al 10 "))
#while usuario!= numero:
 #  cont=cont+1
 #  print("has fallado")
 #  usuario=int(input("vuelve a intentarlo "))
#else:
 # print ("correcto!","has intentado",cont)
#n=1
#suma=0
#while n<=10:
#  suma+=n
#   n+=1
#print(suma)
#numero=1
#num=2
#total=0
#while total<=54:
#  total=numero+num
#  total==numero
#  num+=1
#print(total)
#numero=2
#suma=0
#while numero<=20:
#   suma+=numero
#   numero+=2
#print(suma)
#n=1
#total=0
#while n<=20:
#  if n%2==0:
#    total+=n
 # n+=1
#print(total)
#n=int(input("dame un numero de inicio"))
#p=int(input("dame un numero final"))
#total=0
#while n<=p:
#  if n % 3 ==0:
#    total+=n
#  n+=1
#print(total)
#password="123"
#user="yo"
#try2=input("escribe el usuario ")
#trys=input("escribe la contrasenna ")
#while trys!=password or try2!=user:
#  print ("error")
#  trys=input("vuelve a intentar poner la contrasenna ")
 # try2=input("trata otra vez de poner el usuario ")
#else:
 #   print("correcto has entrado al sistema")
#bandera=True
#puntos=100 
#n=5
#l="b"
#while bandera:
 #    numero=int(input("dame un numero del 1 al 5 "))
  #   letra=input("dame una letra desde la a a la e ")
  #   if numero!=n and letra!=l:
  #    print("has perdido , se te restaron 5 puntos " )
  #    puntos-=5
  #   elif numero!=n or letra!=l:
  #    print("has perdido por poco se te restaron 2 puntos ")
   #   puntos-=2
   #  else:
    #  print("has ganado , te quedaron",puntos)
    #  bandera=False

#print("juego termimado ") 
#a="artefacto"
#cont=0

#while cont<=len(a)-1:
# print(a[cont])
# cont+=1
#vocales="aeiou"
#palabra=input("escribe una palabra ")
#indice=0
#numerovocales=0
#while indice<=len(palabra)-1:
 #    if palabra[indice] in vocales:
 #         numerovocales+=1
  #   indice+=1
#print("el numero de vocales es " , numerovocales)


#v="aeiou"
#p=input("palabreame ")
#i=0
#nv=0
#while i<=len(v)-1:
    # if v[i] in p:
    #      nv+=1
    # i+=1
#print("numero de vocales ",nv ) 
#palabra=input("escribe una palabra")
#vocales="aeiou"
#consonantes="qwrtypsdfghjklzxcvbnm"
#nvocales=0
#ncons=0
#n=0
#while n<=len(palabra)-1:
  #   if palabra[n] in vocales:
  #        nvocales+=1
  #   elif palabra[n] in consonantes:
   #       ncons+=1
   #  n+=1
#print("el numero de vocales es",nvocales,"el numero de consonantes es", ncons)     
#cont=0
#indice=0
#vocales="aeiou"
#palabra=input("escribe una palabra")
#lpalabra=len(palabra)-1
#while indice<=lpalabra:
  # if palabra[indice]in vocales:
   #  cont+=1
  # indice+=1 
#print("l cantidad de vocales es ",cont )
#t=(1,2,3,4,5)
#t_1=t[2:3]
#print(t_1)
#password="kiku"
#n=True
#while n:
#  usuario=input("escribe la contrasenna ")
#  if password!=usuario:
#    print("contrasenna incorrecta ")
#  else:
 #   print("contrasenna correcta ")
 #   n=False
#print("programa terminado ")
# colores=["rojo","amarillo","verde","blanco"]
# bandera=True
# puntos=100
# print("....escala de colores...")
# print("juega un poco...")
# while bandera:
#   usuario=input("escribe 5 colores en 5 turnos  ")
#   if usuario not in colores:
#     puntos-=2
#     print("te has equivocado te quitamos 2 puntos")
#   else:
#     print("has dado con los colores te quedaron",puntos,"puntos")
#     bandera=False
# print("juego terminado")
  
# total=0
# while total<100:
#   numero=int(input("dame un numero"))
#   total+=numero
  
# print("la suma es", total)
#lista=[28,36,43,52,61,75,84,97]
# suma=0
# parado=False
# usuario=int(input("dame un numero "))
# for i in lista:
#   suma=usuario+i
#   if suma ==100:
#       parado=True   
# if parado==True:
#   print("se acabo el programa,el numero cumple con los requisitos ")
# else:
#   print("el numero no cumple con los requisitos")

# user=int(input("dame el numero"))
# if 100 - user in lista:
#   print("esta en la lista")
# else:
#   print("no esta en la lista")
'''''
  para mannana la lista, lista=[28,36,43,52,61,43,75,84,43,97]
 numero=43, se trata de que el programa diga cuantas veces se repite el numero 43 en la lista usando for
'''''
# lista=[28,36,43,52,61,43,75,84,43,97]
# numero=43
# cont=0
# for i in lista:
#   if i==numero:
#     cont+=1
# print("el numero 43 se repite",cont,"veces")
 
# meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
# meses_b=()
# for i in meses:
#    if "b"in i:
#     meses_b+= (i,)
#     print("los meses son ", meses_b)

# lista=[2,5,90,23,45,87,54,11,39]
# elemento=54
# for i in range(len(lista)):
#   if lista[i]==elemento:
#     print("el elemento esta en la lista en la posicion", i+1)
 
# n=int(input("dame un numero "))
# for i in range (1,11):
#  print(n, "*",i,"=",n*i)

#ejercicio
# n=int(input("da el numero "))
# for i in range(1,11):
#   print(n ,"*",i,"=",n*i )

# mostrar temp entre 18 y 25 incluidos,
# indicar en que posicion esta la temperatura erronea
# temperaturas=[19,22,24,23,27,21,20,19,18,21,20]
# busqueda=range(len(temperaturas))
# for i in busqueda:
#   if temperaturas[i]< 18 or temperaturas[i]>25:
#     break
# print("la temperatura es erronea en la posicion ",i+1) 

# for t in temperaturas:
#   if 18<t>25:
#     print("temperatura correcta")
#   else:
#     print("temperatura incorrecta")
#     break

# adivinar letras y te pide letras constantemente hasta que adivines
#la w no eta permitida de salir el programa se para
# l="k"
# bandera=True
# while bandera:
#   letra=input("dame una letra ")
#   if letra!=l:
#    print("incorrecto!")
#    if letra=="w":
#       print("no se puede poner esa letra")
#       break
#   else:
#     print("correcto!")
#     bandera=False 
# print("acabo el programa") 


# ejercicio
# letra="k"
# while True:
#   usuario=input("dame una letra ")
#   if usuario!=letra:
#     print("incorrecto!")
#     if usuario=="w":
#       print("esa letra no la pongas")
#       break
#   else:
#     print("correcto!")
#     break
# print("se acabo el programa")

#ejercicio
# letra="b"
# while True:
#   l=input("dame una letra ")
#   if l!=letra:
#     print("incorrecta")
#     if l=="w":
#       print("no se puede poner esta letra")
#       break
#   else:
#     print("correcto")
#     break
# print("programa terminado ")

# import math
# radio=float(input("dame el radio del circulo "))
# area_circulo=math.pi*radio**2
# print("el valor del area del circulo es",area_circulo)

''''
esta es otra forma de llamar a todos laas funciones del metodo math
"from"+ math import *
'''
# from math import *
# radio=3
# area=pi * radio**2
# print(area)
  
# ejercicio

# a=float(input("dame el numero del primer valor "))

# b=float(input("dame el numero del primer valor "))

# hipotenusa=math.sqr(a**2+b**2)
# print(hipotenusa)

# import math
# r=float(input("dame el radio de la circunsferencia "))
# s=float(input("dame el semi eje de la circunsferencia "))
# p= 2*math.pi *math.sqrt((r**2 + s**2)/2)
# print("el perimetro de la circunferencia es ", p)


#metodo random "randint..." te devuelve un valor aleatorio"#
# import random
# print(random.randint(1,10))

'''''
aleatorio del 1 al 100 numero,
indica mayor o menor que el numero que ha que adivinar
tines 7 intentos, sino cierra el programa y te dice que as perdido 
'''''
# import random 
# numero= random.randint(1,100)
# intentos=0
# op=["estas por el piso", "sube sube que te arrastras", "que no que estas muy bajo"]
# op_1=["demasiado alto papa","que no que no todavia muy alto","tu que cres que esto es una escalera sigue demasiado alto"]
# opcion_a=random.choice(op)
# opcion_b=random.choice(op_1)
# print("jugemos")

# for i in range(8):
#   user=int(input("dame un numero que crees que sea "))
#   intentos+=1
#   if intentos==7:
#     print("te has equivocado,has gastado", intentos,"el numero que tenias que adivinar era ", numero)
#     break  
#   elif user>numero:
#     print(opcion_b,intentos,"intentos")
#   elif user<numero:
#     print(opcion_a,intentos,"intentos")  
#   else:
#     print("has ganado, has necesitado ", intentos,"intentos")
#     break
# print("fin del juego")

# ejercicio#
# import random
# numero=random.randint(1,100)
# op_a=["el numero esta muy alto","todavia muy alto", "por el cielo"]
# op_b=["te has quedado bajo","estas aun muy por debajo","estas por el suelo"]
# opcion=random.choice(op_a)
# opcion_1=random.choice(op_b)
# intentos=0
# for i in range(7):
#   intentos+=1
#   user=int(input("trata de adivinar el numero , introducelo"))
#   if intentos==7:
#     print("ha terminado el juego , has perdido")
#     break
#   elif numero!=user:
#       if user>numero:
#         print(opcion,intentos)
#       elif user<numero:
#         print(opcion_1,intentos)  
#   else:
#     print("felicidades has ganado,has utilizado", intentos, "intentos") 
#     break 
# import random
# print("bienvenido a tertulia ")
# print("comenta tus problemas al doctor")
# comentario_1=["psss y ahi le has dado","tremendo","esa jeva si"]
# comentario=["cuenta, cuenta mas","valla pero que mierda de hitoria","eso es lo que yo digo ","como me dijiste que te llamabas? ","y a mi que me importa eso"]
# opcion=random.choice(comentario)
# opcion_1=random.choice(comentario_1)
# bandera=True
# tiempo=0
# c=3
# while bandera:
#   user=input("responde con sinceridad ")
#   if tiempo>c:
#     print(opcion)
#   elif tiempo<c:
#     print(opcion_1)
#   tiempo+=1
#   if tiempo==10:
#     break
# print("has excedido el tiempo de tertulia")

# import random
# cara=0
# cruz=0
# for i in range(100):
#   tiradas=random.choice(["caras","cruces"])
#   if tiradas=="caras":
#     cara+=1
#   elif tiradas=="cruces":
#     cruz+=1
# print("han salido",cara,"y",cruz,"cruces" ) 

# import random
# op=random.choice(["papel","tijera","piedra"])
# bandera=True
# seguir=""
# while bandera:
#      user=input("juguemos a piedra , papel y tijeras , que vas a elegir? ")
#      if op==user:
#        print(op,"empate")
#      elif op=="papel" and user=="piedra":
#         print(op,"has perdido")
#      elif op=="tijera" and user=="piedra":
#        print(op,"has ganado")
#      elif op=="piedra" and user=="tijeras":
#         print(op,"has perdido")
#      elif op=="piedra" and user=="papel":
#          print(op,"has ganado")
#      else:
#         op=="papel" and user=="tijeras"
#         print(op,"has ganado")
#      seguir=input("quieres seguir jugando s/n ")   
#      while True:
#       if seguir!="s":
#         print("juego terminado")
#         bandera=False
#         break
#       else:
#         break      
  
# ejercicio

# from random import randint
# opcion=randint(1,3)
# piedra=1
# tijera=2
# papel=3
# bandera=True
# while bandera:
#   user=int(input("juguemos , elige piedra 1, tijera 2, papel 3 "))
#   if user==opcion:
#     print ("la maquina ha elegido",opcion,"empate") 
#   elif user!= opcion:
#      if user==1 and opcion==2:
#        print ("la maquina ha elegido",opcion,"has ganado")
#      elif user==1 and opcion==3:
#        print ("la maquina ha elegido",opcion,"has perdido")
#      elif user==2 and opcion==1:
#        print ("la maquina ha elegido",opcion,"has perdido")
#      elif user==2 and opcion==3:
#       print ("la maquina ha elegido",opcion,"has ganado")
#      elif user==3 and opcion==1:
#       print ("la maquina ha elegido",opcion,"has ganado")
#      elif user==3 and opcion==2 :
#       print ("la maquina ha elegido",opcion,"has perdido")
#   else:
#     print("opcion incorrecta")

#   while True:
#          continuar=input("quieres seguir jugando s/n ")
#          if continuar!="s":
#           print("juego terminado")
#           bandera=False
#           break
#          else:
#              break
# import random
# import time
# t_inicio=time.time()
# puntos=0
# while True:
#   n_1=random.randint(1,9)
#   n_2=random.randint(1,9)
#   op=random.choice(["*","+"])
#   if op=="*":
#     resultudo=n_1*n_2
#     print(n_1,op,n_2,end="")
#   elif op=="+":
#     resultado=n_1+n_2
#     print(n_1,op,n_2,end="")
#     respuesta=int(input("="))
#   if respuesta==resultado:
#     puntos+=1
#     print("correcto,tienes",puntos,"puntos")
#   elif respuesta!=resultado:
#     print("incorrecto, tienes",puntos,"puntos")
#   final=time.time()
#   if final-t_inicio>=10:
#     print("se acabo el tiempo")
#     break
# print("juego terminado") 
# print("has alcanzado",puntos,"puntos")
# import time
# inicio=time.time()
# for i in range (21):
  
#   a=time.sleep(.5)
#   final=time.time()
#   print(((20-i)/2),"tiempo transcurrido",final-inicio -1)

#ejercicio

# import time
# inicio=time.time()
# for i in range(10,-1,-1):
#  time.sleep(1)
#  final=time.time()

#  print(i,"tiemppo transcurrido ",final-inicio-1)

# import time
# import random
# colores=["azul","verde","amarillo","blanco"]
# puntos=0
# seguir=True
# for i in range(len(colores)):
#   random.shuffle(colores)
   
#   print("adivina los colores ...")
#   time.sleep(3)
#   print("estas listo")
#   time.sleep(2)
#   print("ahora")
#   print(colores)
#   time.sleep(2)
  
#   for i in range(10):
#     print(" ", "*"*5)
#   for i in range(10,0,-1):
#    print(" ","*"*4)
#   print("")

#   print("introduce los colores")
#   user=input("introduce el primer color ")
#   if user==colores[0]:
#      puntos+=1
#      print("has adivinado el primer colores color tienes ", puntos)
#   else:
#       print("te has equivocado")
#       break
#   user_1=input("introduce el segundo color ")
#   if user_1==colores[1]:
#      puntos+=1
#      print("has adivinado el segundo color tienes ", puntos)
#   else:
#     print("te has equivocado") 
#     break 

#   user_2=input("introduce el tercer color ")
#   if user_2==colores[2]:
#      puntos+=1
#      print("has adivinado el tercer color tienes ", puntos)
#   else:
#     print("te has equivocado") 
#     break 
     
#   user_3=input("introduce el cuarto color ")
#   if user_3==colores[3]:
#      puntos+=1
#      print("felicidades has adivinado tienes ", puntos)
#   else:
#     print("te has equivocado") 
#     break
  
#   print("obtuviste  ", puntos)
#   print("")
# ejercicio
# import time
# import random
# colores=["blanco","amarillo","verde","azul","rojo","negro","rosado","violeta","carmelita","naranja"]
# puntos=0
# bandera=True
# a=""
# while bandera:
#   print("****juego de colores**** ")
#   print("adivina los cuatro colores")
#   print("")

#   print("estas preparado...")
#   time.sleep(2)
#   print("ahora ")
#   time.sleep(1)

#   a=random.sample(colores,4)
#   for i in range(len(a)):
#     print("",a[i],end="")
#   print("")

#   time.sleep(2)

#   for i in range (10):
#     print("*"*i*5)
#   for i in range(10,0,-1):
#      print("*"*i*5)

#   user=input("escribe el primer numero ")  
#   user_1=input("escribe el segundo numero ") 
#   user_2=input("escribe el tercer numero ")
#   user_3=input("escribe el cuarto numero ")
#   print("")

#   if user==a[0]:
#     puntos+=1
#     print("has adivinado el primer numero tienes ", puntos)
#   else:
#     print(" te has equivocado")
#     break

#   if user_1==a[1]:
#     puntos+=1
#     print("has adivinado el segundo numero tienes ", puntos)
#   else:
#     print(" te has equivocado")
#     break

#   if user_2==a[2]:
#     puntos+=1
#     print("has adivinado el tercer numero tienes ", puntos)
#   else:
#     print(" te has equivocado")
#     break

#   if user_3==a[3]:
#     puntos+=1
#     print("has adivinado el cuarto numero tienes ", puntos)
#   else:
#     print(" te has equivocado")
#     break
#   print("has obtenido " ,puntos)
#   seguir=input("quieres volver a jugar , s/n" )
#   while True:
#     if seguir == "s":
#      break
#     else:
#       bandera=False 
#       break
#   print("se ha terminado el juego ")
  
  
'''''
entramos a los metodos , metodos de streams : upper para mayusculas, lower para minusculas, title para cambiar la primera letra a minuscula

''''' 
# las funciones pre, "imput" para poder usar varias cadenas de caracteres se tienen que concatenar,"+"

# print ("hola")
# bandera=True
# while bandera:
#   nombre=input("cual es tu nombre ? ")
#   if nombre==nombre or nombre.lower()==nombre:
#      print("bien")
#      print("bienvenido ", nombre.title())
#      print("")

#   print("seguro que eres ", nombre.upper(),"? ")
#   otravez=input("s/n")
#   while True:
#      if otravez=="s":
#       print("perfecto solo comprobaba ") 
#       bandera=False
#       break
 
''''
  metodos strip, split.  
metodo strip para quitar espacios o caracteres de los extremos de la cadena.
metodo split para separar streams y devolverlos en forma de lista.
variable.strip("cadena")
variable.split("cadena")
 
 * diferencias entre metodos y funciones , los metodos van a ser especificos para objetos
  

'''''
#"recoger todas las plabras y devolverlas sin comas o puntos"
# metodo format que devuelve una nueva cadena de caracteres ,
# v=v.format{"fulano","esperansejo"}
# "hola {}.".format("jose")
# "hola {} {}.".format("jose", "gonzales")
# " hola {0} {1} .". format("jose","gonzales")
# " hola {n} {a} .". format(n="jose",a="gonzales")


# ejercicio

# while True:
#   print("carta de presentacion")
#   print("indque los siguientes datos : ")
#   tratamiento=input(" sr/sra ")
#   nombre=input("nombre ")
#   apellido=input("apellido ")
  
#   print("{}  {} {} :".format(tratamiento.title(),nombre.title(),apellido.title()))

#   if tratamiento.lower()=="sr":
#     print("por la presente se le invita  la fiesta")
#   elif tratamiento.lower()=="sra":
#     print("por la presente se le invita  la fiesta")

#   seguir=input("desea mandar otra carta s/n ")
#   if seguir!="s":
#        break
 #ejercicio de strip i split
#cadena= " en la arena , habia muchas conchas. Por que ?, aun no se sabe . "
# palabra=cadena.split()
# for i in palabra:
#   p=i.strip(".")
#   c=p.strip(",")
#   print(c)
# ejercicio con format
# while True:
#     print("presentacion para la fiesta")
#     formal=input("indique sr o sra ")
#     nombre=input("diga su nombre ")
#     apellido=input("diga su apallido ")
#     print("{} {} {}".format(formal.title(),nombre.title(), apellido.title()))
#     print()
#     if formal.lower()=="sr":
#       print("estimadisimo sennor",nombre,apellido,"usted ha sido invitado a la fiesta")
#     elif formal.lower()=="sra":
#         print("estimadisima sennora",nombre,apellido,"usted ha sido invitada a la fiesta")
#     else:
#         print("pase equivocado")
#     print()    
 
#     seguir=input("desea volver a mandar otra carta de invitacion ? (s/n)")
#     if seguir!="s":
#       break
# print("se ha acabado el programa ")

'''''
 otro metodo y formas :
center ... v.center(), se utilza para central dicha variable
dentro de los parametros se pueden poner nuevos parametros 
ej: print(" {1:12d} * {2:12,2f}={3:2f}". format(v1,v2,v1*v2) )
el  numero del medio reprenta los espacios y el de mas a la derecha
representa cuantos decimales quieres que contenga.
la d y la f significan:
d= int
f=float

'''''
# metodos de listas:
# append : v.appen(100)... solo admite un solo elemnto y se utliza para modificar el contenido de las listas

# v=[]
# for i in range(1,101):
#   v.append(i)
#   print(v)

'''''
* en este ejercicio , pusiste pares=numeros.append(i)
si lo haces de este modo no te devuelve ninguna lista 
pares.append(i)   para agreagar nuevos valores a una nueva lista
* tambien pusiste un prin para que devolviese las listas pares e impoares 
seguido de los condicionales , en ese caso por el ciclo for
te deulve los indices de las listas uno a uno lo que lo hace 
dificil de entender hasta el final
lo mas correcto era poner los print al final fuera del ciclo , al menos en este caso
* con el metodo append como lo que hace es modficar, es necesario
crear la lista al igual que el metodo shuffle.
'''''
# pares=[]
# impares=[]
# numeros=[2,3,5,8,9,12,21,24,25,28]
# for i in numeros:
#   if i % 2 == 0:
#    pares.append(i)
   
#   elif i % 2 !=0:
#     impares.append(i)
      
#   else:
#     print("numero irregular")
#     break 
# print("lista de impares ",impares)
# print("lista de pares ", pares)
'''''
* debes poner un atributo en el metodo append(*)
para que puede modificar la lista 
'''''
# ejercicio

# productos_final=[]

# while True:
#   productos=input("que productos deseas comprar ")
#   productos_final.append(productos)
#   seguir=input("deseas comprar mas productos (s/n)")
#   if seguir!= "s":
#     break
  
# print(productos_final)

# otra forma de hacer este ejercicio
'''''
* de esta forma se optimiza mas el codigo haciendolo mas elegante

'''''
# print(" lista de compra")
# producto=[]
# while True:
#   user=input("pon el producto que desea comprar ('n'para salir) ")
#   if user=="n":
#    print("compra terminada ")
#    break
#   else:
#     producto.append(user)
# print("el total de productos es : ",producto)

# ejercicio
'''''
con el metodo append es necesario ,dado el caso de una lista
modificada por dicho metodo ,al guardarla en una nueva variable 
; se tiene que gurdar la lista modificada en una lista nueva  

# n=[1,2,3]
# m=[4,5]
# # n.extend(m)
# # print(n)
# k=[]
'''''
# n.append(m)
# k=n
# print("con append",k)

# s=[1,2,3,4]
# d=[5]
# s.extend(d)
# print(s)

# metodo de lista extend .... 
'''''
con este metodo se puede modificar una lista agregando elementos nuevos etc
la diferenca entre el metodo append y extend es que append devolveria si se le pasase por 
parametro una lista , pasaria la lista completa llaves y todo dentro de la lista
modificada .
 s=[1,2,3,4]
 d=[5]
 s.extend(d)
 print(s)
'''''

# metodo de lista : insert
'''''
 este metodo iserta un numero dentro de una lista entre sus indices
 ej s=[1,2,3,4]
    d=[5]
    s.insert(3,s)
    print(s)
    se le tiene que pasar 2 argumentos el 1ro representa donde va a insertar
    ten wn cuenta que tienes que contar desde 0,
    s=[1,2,3,4]
           0,1,2,3....respectivamente.
   en este caso ademas par no annadir las llaves a la lista de numwros
   cuando insertas tienes que poner 
      s=[1,2,3,4]
      d=[5]
      s.insert(3,d[5])
      print(s)
   de esta forma insertas solo el indice 
'''''

# ejercicio
# crear una lista desde 1 al 5
# m=1
# n=[2,3]
# s=[4]
# t=5
# n.insert(0,m)
# n.extend(s)
# n.append(t)
# print(n)

'''''
operador "none" y  operador "is"
* el operador none solo se puede comparar con el mismo.
te sirve para asignar una variable de tipo vacio.
* el oprtador is es para comparar por identidad.
ej: if a is none
: la identidad de las listas es distinto.
'''''
# ejercico

# debe salir el nnumero mayor de 5 numeros
'''''
en este ejercicio te equivocaste en igualar la variable n con mayor  (==, =)
tmbien tienes que tener en cuenta el operador is ...
'''''
# mayor=None
# for i in range(5):
#     n=int(input("dame un numero "))
#     if mayor is None or n > mayor:
#       mayor=n
# print("el numero mayor es ", mayor)

# otro ejrcicio
#tres jugadores que introduzcan un numero y
# espera a que los tres jugadores hayan puesto el numero

# jugador_1=None
# jugador_2=None
# jugador_3=None


# while jugador_1 is None or jugador_2 is None or jugador_3 is None:
#       print("***** seleccion de jugadores *****".center(50))
#       print()
#       seleccion=int(input("presiona 1 para jugador_1 , 2 para jugador_2 , 3 para jugador_3 "))
#       if seleccion == 1:
#         jugador_1=int(input("introduce el numero "))
#       elif seleccion==1 and seleccion is not None:
#         print("el jugador 1 ya ha elegido ")  
#       elif seleccion == 2:
#          jugador_2=int(input("introduce el numero "))
#       elif seleccion==2 and seleccion is not None:
#         print("el jugador 1 ya ha elegido ") 
#       elif seleccion == 3:
#           jugador_3=int(input("introduce el numero "))
#       elif seleccion==3 and seleccion is not None:
#         print("el jugador 1 ya ha elegido ")     
#       else:
#         print("has puesto un valor incorrecto ")
# print("los tres jugadores ya han elegido numero ")
# print("jugador 1", jugador_1)
# print("jugador 2", jugador_2)
# print("jugador 3", jugador_3)

'''''
funciones predeterminadas list(), tuple().
*para tuple se le tiene que pasar elementos iterable, varios numeros o listas
*para copiar una lista . se utiliza la funcion list() 
q=list(1,2,3,4) 
de esta forma se queda esta lista guardada en q , de manera que si se le agregace un nuevo 
valor a la lista puedes mantener la lista original

'''''
# ejercicio
# crear lista vacia utilizando funciones
# annadir la letra a a la lista usando metodos
#haz una copia de lista creando una lista distinta y comprueba los elementos
# annadir una b a la copia

# letras=list()
# letras.append("a")
# copia=list(letras)
# copia.append("b")
# print(letras)
# print(copia)

# otro ejercicio

# lista en reverso

# numeros=[1,5,8,4,7,2,9]
# reverso=list()
# for i in range(len(numeros)):
#   reverso.append(numeros[len(numeros)-1-i])
  
# print(reverso)

'''''
otra forma
operador de indexacion
'''''
# numeros=[1,5,8,4,7,2,9]
# reverso=list()
# reverso=numeros[6::-1]
# print(reverso)
'''''
otra forma nueva
* esta forma hace que de uno a uno el indice de la lista va de atras hacia delante     
'''''
# reverso=list()
# numeros=[1,5,8,4,7,2,9]
# for i in numeros:
#   reverso=[i]+ reverso
#   print(reverso)
'''''
otra forma con el metodo reverse
* este metodo solo modifica por lo cual a la lista que se quiere modificar primero tienes que hacerle una copia. 
de lo contrario devolveria el metodo none
'''''
# numeros=[1,5,8,4,7,2,9]
# numeros.reverse()
# print(numeros)

'''''
metodo sort y funcion sorted
* este metodo ordena la lista , pero como el metodo reverse , modifdica la lista
* utilizando lista.sort(lista.reverse=True).... ordena la lista de mayor a menor
con sorted , devuelve una lista segun el iterable 
'''''
# lista=[1,2,3,4,5]
# lista_nueva=list(lista)
# lista_nueva.sort(reverse=True)
# print(lista)
# print(lista_nueva)

# lista_nueva_b=sorted(lista_nueva, reverse=True)
# print(lista_nueva_b)

# ejrcicio
'''''
hacer un programa en el que halla que elegir contrasenna
la contrasenna tiene que tener de 8 a 15 caracteres, 1 mayuscula
1 minuscula, 1 dijito, 1 caracter especial: @$%&
habra 5 intentos,despues de cada intento,se indicara la causa
y al final del 5 se indicara que ha sido imposible establecer
contrasenna.
'''''
# contrasenna=None
# intentos=0
# mayuscula="QWERTYUIOPASDFGHJKLZXCVBNM"
# minuscula="qwerttyuiopasdfghjklzxcvbnm"
# digito="1234567890"
# especial="$%&@"
# bandera=True
# while bandera:
#       intentos+=1
#       user=input("introduce contrasenna ")
#       mayu=False
#       min=False
#       long=False
#       dig=False
#       esp=False

#       if len(user)>7 and len(user)<16:
#         long=True
#       for caracter in user:  
#          if caracter in mayuscula:
#             mayu=True
#          if caracter in minuscula:
#              min=True
#          if caracter in digito:
#             dig=True
#          if caracter in especial:
#             esp=True 
#       if long and mayu and min and dig and esp:
#          print("la contrsenna esta correcta ")
#          contrasenna = user
#          bandera=False
#       else:
#         if not long:
#           print("la contrasenna debe de tener entre 8 y 15 caracteres ")
#         elif not mayu:          
#           print("la contrasenna debe de tener al menos una mayuscula ")
#         elif not min:
#           print("la contrasenna debe de tener minusculas ")
#         elif not dig:
#           print("la contrasenna debe de tener al menos un digito ")
#         elif not esp:
#            print("la contrasenna debe de tener al menoa un caracter especial ($,%,&,@)")      
#       if intentos > 4:
#         bandera = False
# if contrasenna :
#    print("la contrasenna es : {}".format(contrasenna))
# else:
#   print("no se ha podidio establecer contrasenna ")
'''''
dar formato a cadenas de caracteres 
'''''
# operador de formato (se utiliza con el simbolo %)
# mertodo format...
# metodo f strings
'''''
* con el metodo f string puedes concatenar elementos o conjuntos de listas o tuplas de esta 
forma....
* tambien puedes agregar operadores para reservar espacios ...
'''''
# lista=[1,2,3,4,5]
# precio=[12,13,14,15,16]
# for i in range(len(lista)):
#   print(f"el numero de lista {lista[i]} es {precio[i]}")

# for i in range(len(lista)):
#   print(f"el numero de lista {lista[i]:10} es {precio[i]:10}")

# ejercicio 
# hallar la primera palabra mas larga
'''''
* en este ejercicio se utiliza una variable para compararla con los elementos de una lista 
(len(palabra) ) 
* en el caso que quisieramos hallar la palabra mas larga pero la ultima habria que agreagar
el sigo de igual en conjunto con el signo de comparacion, recuerda que con este signo
los caracteres "letras", se comparan segun el abecedario. 
'''''
# lista_palabras=["mesa","armario","silla","lampara","cuadro"]

# palabra_maslarga=None
# long_mayor=0
# for palabra in lista_palabras:
#   if len(palabra) > long_mayor:
#     long_mayor=len(palabra)
#     palabra_maslarga = palabra
# print(f"la palabra mas larga es {palabra_maslarga} con una longitud de {long_mayor}") 

'''''
metodos de cadenas de caracteres 
* index
* find
estos metodos tamben se les puede pasar parametros para encontrar subcadenas

'''''
# palabra="zanahoria"
# letra_h= palabra.find("h", 3)
# print(letra_h)

# letra_i=palabra.index("i",6)
# print(letra_i)

'''''
desempaquetado de tuplas
* los mismos valores tanto letras como numeros, en caso de que halla mas letras que numero o viceversa
daria error a no ser ....
* con el signo "*"no importa cuantos valores o letras , este va a tomar el resto de los valores 
* en caso de tener una sola variable se le puede pasar el resto de numero haciendola tupla...
'''''
# a,b,c=1,2,3
# print(a,b,c)
# a,b,*c=1,2,3,4
# print(a,b,c)
# lista=[1,2,3]
# *a,=lista
# print(a)
'''''
for anidados 
'''''
# ejercicio
# crear baraja con bucles , annadiendo dichas cartas a una lista 

# tantos=["a","2","3","4","5","6","7","s","c","r"]

# palos=["oros","copas","espadas","bastos"]

# baraja=[]

 
# for i in tantos:
#    for b in palos:
#     carta="{} de {}".format(i,b)
#     baraja.append(carta)
# print(baraja)
# # en este primer ejemplo con los for anidados obtenemos una lista desordenada. 
# for i in range(0,40,4):
#   print("{} {} {} {}".format(baraja[i],baraja[i+1],baraja[i+2],baraja[i+3]))
# # recuerda que (0,40,4)representan que desde (0 hasta 40)va a estar utilizando 4 indices.
# # es decir : 0123 ,4567 , 8910....
# for i in range (0,40,4):
#   for b in range(4):
#     print("{:16} ".format(baraja[i+b]),end="" )
#   print()
  
# aqui esta el codigo optimizado , para cada iteracion del bucle externo se le suma la 
# iteracion del bucle interno , luego agregando el metodo format y quitando los espacios para
# que no salte de linea internamente y con el otro print salte externamente .

# ejercicio
'''''
* tabla de multiplicar del 2 al 7 utilizando el for anilldo.
'''''
# en este caso solo tenias que utilizar el ciclo anaidado nada mas y darle espacios 
#con saltos de linea 
# for numero in range(1,11):
#    for i in range (2,8):
#       print("{:2} * {:2} = {:2} ".format(i,numero,i*numero),end="") 
#    print()   
    



