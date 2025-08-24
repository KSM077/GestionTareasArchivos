import json
import os


ID = 1
tasks = []

def menu():
    print(" ---------------- Menu: ----------------\n"
    "1. Añadir nueva tarea \n"
    "2. Buscar tarea por ID \n"
    "3. Listar todas las tareas \n"
    "4. Eliminar tarea por ID \n"
    "--------------------------------------")
    choice = int(input("Seleccione una opción (Digitando el número): "))
    return choice


def add_task():
    
    global ID
    task = input("Ingrese la tarea: ")
    desc = input("Ingrese la descripción de la tarea: ")

    user_data = {
        "ID": ID,
        "Task": task,   
        "Description": desc
    }
    
    tasks.append(user_data)

    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)
        ID += 1
    print(f"Se ha logrado añadir la tarea correcamente con ID: {ID} \n")


def search_task():
    global ID
    search_ID = int(input("Ingrese el ID de la tarea que desea buscar: "))

    with open("task.json", "r") as file:
        tasks = json.load(file)

    for task in tasks:
        if task["ID"] == search_ID:
            print(f"Tarea encontrada: ID: {task['ID']}, Tarea: {task['Task']}, Descripción: {task['Description']}")
        else:
            print("Tarea no encontrada.")

def list_tasks():

    with open("task.json", "r") as file:
        tasks = json.load(file)
    
    for task in tasks:
        print(f"ID: {task['ID']}, Tarea: {task['Task']}, Descripción: {task['Description']}")
        


def delete_task():

    ...

  
  
  

while True:
    menu()
    choice = menu()
    if choice == 1:
        add_task()
    elif choice == 2:
        search_task()
    elif choice == 3:
        list_tasks()
    elif choice == 4:
        delete_task()

    continuar = input("¿Desea agregar otra tarea? (s/n): ").lower()
    if continuar != 'n':
        continue
    else:
        print("Saliendo del programa.")
        break

    
    
