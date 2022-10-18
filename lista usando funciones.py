nombres=input("escribe los nombres  ")
lista=nombres.split(",")
print(lista)
def buscar_nombres(u=""):
 
  while True:
      
      if u in lista:
         return ("se encuentra")
      else:
           return("no se encuentra")
       
usuario=input("escribe el nombre a buscar ")
user=buscar_nombres(usuario)
def posicion():
  cont=0
  for i in lista:
     if usuario!=lista[i]:
       cont+=1
     if usuario==lista[i]:  
       return ("esta en la posicion",cont)
poss=posicion  
print(user,poss)
