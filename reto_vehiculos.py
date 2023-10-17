# https://replit.com/join/ykvsxorzyd-frida-paulinapa

#clasificar autos 
ruedas = int(input("¿Cuantas ruedas tiene tu auto? "))
print(" ")
combustible =input("¿Que tipo de combustible utiliza tu auto? (gasolina, diésel,electricidad) ")
print(" ")
emisiones = float(input("¿Numero de emisiones en gramos que hace tu auto? "))

if ruedas == 4 and combustible == "electricidad":
  print("Este es un vehiculo electrico")
elif ruedas > 4 and combustible == "gasolina" and emisiones > 150:
  print("El vehiculo es grande y contaminante")
elif combustible == "diesel" :
  print("El vehiculo utiliza diesel")
elif combustible == "gasolina" :
  print("Este vehiculo utiliza gasolina")
else:
  print("No tenemos una clasificacion para este vehiculo :(")
