import json


ID = 1
tasks = []




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
            print(f"Tarea encontrada: ID: {task['ID']}, Tarea: {task['Task']}, Descripción: {task['Description']} \n")
        else:
            print("Tarea no encontrada. \n")

def list_tasks():

    with open("task.json", "r") as file:
        tasks = json.load(file)
    
    for task in tasks:
        print(f"ID: {task['ID']}, Tarea: {task['Task']}, Descripción: {task['Description']} \n")



def delete_task():

    delete = int(input("Ingrese el ID de la tarea que desea eliminar: "))

    with open("task.json", "r") as file:
        tasks = json.load(file)
    for task in tasks:
        if task["ID"] == delete:
            tasks.remove(task)
            with open("task.json", "w") as file:
                json.dump(tasks, file, indent=4)
            print(f"Tarea con ID {delete} eliminada correctamente. \n")
            break
    else:
        print("Tarea no encontrada. \n")
  
  
  

while True:
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

    choice = menu()
    if choice == 1:
        add_task()
    elif choice == 2:
        search_task()
    elif choice == 3:
        list_tasks()
    elif choice == 4:
        delete_task()
    else: 
        print("Saliendo del programa...")

    continuar = input("¿Desea agregar otra tarea? (s/n): ").lower()
    if continuar != 'n':
        continue
    else:
        print("Saliendo del programa.")
        break

    
    
