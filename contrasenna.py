mayuscula="QWERTYUIOPASDFGHJKLZXCVBNM"
minuscula="qwertyuiopasdfghjklzxcvbnm"
numero="1234567890"
caracter_especial="$%&@"
bucle=True
c_esp=False
num=False
mayu=False
min=False
long=False
from time import sleep

print("**** programa para seleccion de contrasenna **** ".center(50))
sleep(1.5)
while bucle:
     user=input("introduce contrasenna ")
     
     for intentos in range (5):
        
        for caracter in user:
         
          if caracter in mayuscula:
            mayu =True
            
          if len(user)>7 and len(user)<16:
            long=True
            
          if caracter in minuscula:
            min=True
            
          if caracter in numero:
            num=True 
               
          if caracter in caracter_especial:
            c_esp=True
            
        if long and min and num and c_esp and mayu:
            print("contrasenna aceptada ")
            bucle=False
        else:
           if not long :
                  print("los caracteres tenen que estar entre 8 y 15 ")
                  break
                 
           elif not mayu:
                 print(" la contrasenna debe de tener al menos una mayuscula ")
                 break
           
           elif not min:
                 print(" la contrasenna debe de tener al menos una minuscula ")
                 break
           
           elif not c_esp:
                print(" la contrasenna debe de tener al menos un caracter especial ($%&@) ")
                break
           
           elif not num:
                print(" la contrasenna debe de tener al menos un digito ")
                break 
       
        if intentos == 4:
                print("has alcanzado un maximo de 5 intentos, contrasenna no establecida ")
                break
        break       
seguir=input("deseas volver a intentar s/n ")
     
if seguir!="s":
            
  bucle = False        
print("programa terminado ".center(50))

