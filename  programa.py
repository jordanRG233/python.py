print ("***** juego de piedra , papel y tijeras ***** ".center(50))
print ("***** en 5 turnos veremos quien optiene mas puntos *****".center(50))
print()
import random
import time
user_1=[]
user_2=[]
total=0
moneda=["cara", "cruz"]
bandera=True
tijera=1
piedra=2
papel=3

while bandera:
     while True:
          comp=random.choice(moneda)
          print("ahora veremos quien empieza ")
          user=input("escoge cara o cruz ")
          if user == comp:
            print("has acertado empiezas tu")
            break
          elif user != comp:
             print("la computadora ha sacado ", comp ,"y tu ", user)
             print("turno del otro jugador ")
             break
          else:
             print("pusiste algo equivocado, (q) para volver a intentar ")
          intentar=""
          if intentar=="q":
             bandera=False
      
     print()
     time.sleep(2.5)
     print("***** hora de juego *****".center(50)) 
     
     
     for i in range(6 -1):
       comp=random.randint(1,3)
       user=input("escribe 1 para tijera, 2 para piedra o 3 para papel ")
       if user == comp:
          print("has empatado")
          i=0
       else:
          if user == 1 and comp == 2:
            print(" has perdido ")
            user_1.append(0)
          elif user==1 and comp == 3:
            print("has ganado ") 
            user_1.append(1) 
          elif user==2 and comp == 1:
            print("has ganado ") 
            user_1.append(1) 
          elif user==2 and comp == 3:
            print("has perdido ") 
            user_1.append(0) 
          elif user==3 and comp == 1:
            print("has perdido ") 
            user_1.append(0) 
          elif user==3 and comp == 2:
            print("has ganado ") 
            user_1.append(1)  
        
     for i in user_1:
          total=user_1[i]
     print("has terminado tu turno " , user_1 , "has terminado con un total de " ,total, "puntos")
     time.sleep(2.5)
     print("turno del otro jugador ")
     
     for i in range(6-1):
        time.sleep(2.5)
        print("***** hora de juego *****".center(50)) 
        time.sleep(1.5)
        comp=random.randint(1,3)
        user=input("escribe 1 para tijera, 2 para piedra o 3 para papel ")

        if user == comp:
          print("has empatado")
          i==0
        else:
          if user == 1 and comp == 2:
            print(" has perdido ")
            user_2.append(0)
          elif user==1 and comp == 3:
            print("has ganado ") 
            user_2.append(1) 
          elif user==2 and comp == 1:
            print("has ganado ") 
            user_2.append(1) 
          elif user==2 and comp == 3:
            print("has perdido ") 
            user_2.append(0) 
          elif user==3 and comp == 1:
            print("has perdido ") 
            user_2.append(0) 
          elif user==3 and comp == 2:
            print("has ganado ") 
            user_2.append(1)  
        
        for i in user_2:
          total=user_2[i]
     print("has terminado tu turno " , user_2 , "has terminado con un total de " ,total, "puntos")   
