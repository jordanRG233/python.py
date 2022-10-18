from tkinter import N


nombres=input("introduce los nombres :")
cont=0
usuario=input("indica el nombre ha chequear :")
def nombre_a_chequear(chequea_nombre):
   for i in nombres:
      if i==chequea_nombre:
        return True
      else:
        return False
       
parametro=nombre_a_chequear(usuario)
print(parametro)
      
  
        

        
