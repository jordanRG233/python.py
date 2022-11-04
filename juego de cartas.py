
atributos=["a","2","3","4","5","6","7","8","9","10","j","q","k",]
elementos=["picas","trebol","corazon","hoja"]
cartas=[]


for i in range(len(atributos)):
  for j in range(len(elementos)):
    variable=f"{atributos[i]} de {elementos[j]} "
    cartas.append(variable)

for k in range(0,50,4):
    for t in range (4):
       print(f"{ cartas[ k+t ]:20} ", end="")
    print()