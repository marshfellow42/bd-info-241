import os
import sqlite3

all_id = []

script_dir = os.path.realpath(os.path.dirname(__file__))

db_path = os.path.join(script_dir, 'tasks.db')

conexao = sqlite3.connect(db_path)

conexao.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        description TEXT,
        completed INTEGER
    );
''')

def create_task(description):
    conexao.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))

def list_tasks():
    cursor = conexao.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    
    if not tasks:
        print("Não têm tarefas disponíveis.")
        return False
    else:
        for task in tasks:
            print(f"ID: {task[0]}, Descrição: {task[1]}, Completada: {'Sim' if task[2] else 'Não'}")
            all_id.append(task[0])
        return True

def mark_completed(task_id):
    conexao.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))

def delete_task(task_id):
    conexao.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

while True:
    print("""
1) Criar uma tarefa
2) Mostrar todas as tarefas existentes
3) Marcar uma tarefa como completo
4) Deletar a tarefa
5) Sair
""")
    decisao = int(input("O que você deseja fazer? "))

    match decisao:
        case 1:
            input_tarefa = input("Qual a descrição da sua tarefa? ")
            create_task(input_tarefa)
        case 2:
            list_tasks()
        case 3:
            if list_tasks():
                while True:
                    choose_task_to_complete = int(input("Selecione o id da tarefa que deseja marcar como completo: "))
                    if choose_task_to_complete in all_id:
                        mark_completed(choose_task_to_complete)
                        break
                    else:
                        print()
                        print("ID inválido. Por favor, tente novamente.")
                        print()
        case 4:
            if list_tasks():
                while True:
                    choose_task_to_delete = int(input("Selecione o id da tarefa que deseja deletar: "))
                    if choose_task_to_delete in all_id:
                        delete_task(choose_task_to_delete)
                        break
                    else:
                        print()
                        print("ID inválido. Por favor, tente novamente.")
                        print()
        case 5:
            break

conexao.close()