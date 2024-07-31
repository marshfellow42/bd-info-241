import sqlite3

conexao = sqlite3.connect("tasks.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        description TEXT,
        completed INTEGER
    );
''')

conexao.commit()

def create_task(description):
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
    conexao.commit()

def list_tasks():
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Description: {task[1]}, Completed: {'Yes' if task[2] else 'No'}")

def mark_completed(task_id):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conexao.commit()

def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conexao.commit()

while True:
    print("""1) Criar uma tarefa
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
            list_tasks()
            choose_task_to_complete = int(input("Selecione o id da tarefa que deseja marcar como completo: "))
            mark_completed(choose_task_to_complete)
        case 4:
            list_tasks()
            choose_task_to_delete = int(input("Selecione o id da tarefa que deseja deletar: "))
            delete_task(choose_task_to_delete)
        case 5:
            break

    input()
    
cursor.close()
conexao.close()