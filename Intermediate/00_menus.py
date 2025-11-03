import os, time

def menu():
  while True:
    os.system("cls")
    print("---MENÚ---")
    print("1) sortir")
    print("2) Opción 2")
    print("3) Opción 3")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
      print("Sortint...")
      time.sleep(1)
      break # Fa que surti del programa

    elif opcion == "2":
      print("Pepe")
      time.sleep(2)
      input("Pulsa ENTER para continuar...")

    elif opcion == "3":
      print("Juan")
      time.sleep(2)
      input("Pulsa ENTER para continuar...")

menu()
