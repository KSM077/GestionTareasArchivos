import json


def menu():
    print(" ---------------- Menu: ----------------\n"
    "1. Añadir nueva tarea \n"
    "2. Buscar tarea por ID \n"
    "3. Listar todas las tareas \n"
    "4. Eliminar tarea por ID \n"
    "5. Salir \n"
    "--------------------------------------")
    choice = int(input("Seleccione una opción (Digitando el número): "))
    return choice


def add_task():

    task = input("Ingrese la tarea: ")
    desc = input("Ingrese la descripción de la tarea: ")
    task_data = {task: desc}
    with open("task.json", "w") as file:
        json.dump(task_data, file, indent=4)

    
  

def search_task():
    task_id = input("Ingrese el ID de la tarea a buscar: ")

  
  

def list_tasks():

    ...

  
  

def delete_task():
    task_id = input("Ingrese el ID de la tarea a eliminar: ")

    ...

  
  
  

while True:
    menu()

    add_task()