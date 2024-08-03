import os
import sqlite3

# Caminho para o banco de dados SQLite
script_dir = os.path.realpath(os.path.dirname(__file__))
db_path = os.path.join(script_dir, 'dbalunos.db')

# Cria a tabela se não existir
def initialize_db():
    with sqlite3.connect(db_path) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS TB_ALUNO (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno varchar(50),
                endereco varchar(100)
            );
        ''')

# Inicializa o banco de dados
initialize_db()

# Inicia o servidor FastAPI
os.chdir(script_dir)
os.system("uvicorn main:app --reload")
