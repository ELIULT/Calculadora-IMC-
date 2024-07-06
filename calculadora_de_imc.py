# Calcuñadpra IMC

def calcular_imc():
  
  nombre = input("Nombre: ")
  apellido_paterno = input("Apellido Paterno: ")
  apellido_materno = input("Apellido Materno: ")

  while True:
    try:
      edad = int(input("Edad: "))
      if edad >= 0:
        break
      else:
        print("Corregir Edad.")
    except ValueError:
      print("Checar tu edad.")

  while True:
    try:
      peso = float(input("Peso:"))
      if peso >= 0:
        break
      else:
        print("Corregir Peso.")
    except ValueError:
      print("Checar Peso.")

  while True:
    try:
      estatura = float(input("Estatura:"))
      if estatura >= 0:
        break
      else:
        print("Corregir Estatura")
    except ValueError:
      print("Checar Estatura")

  imc = peso / estatura ** 2

  datos = {
      "nombre": nombre,
      "apellido_paterno": apellido_paterno,
      "apellido_materno": apellido_materno,
      "edad": edad,
      "peso": peso,
      "estatura": estatura,
      "imc": imc
  }

  return datos

def mostrar_resultados(datos):
  
  print(f"\nDatos del usuario:")
  print(f"Nombre: {datos['nombre']} {datos['apellido_paterno']} {datos['apellido_materno']}")
  print(f"Edad: {datos['edad']} años")
  print(f"Peso: {datos['peso']} kg")
  print(f"Estatura: {datos['estatura']} m")
  print(f"\nÍndice de Masa Corporal (IMC): {datos['imc']:.2f}")

datos = calcular_imc()
mostrar_resultados(datos)
