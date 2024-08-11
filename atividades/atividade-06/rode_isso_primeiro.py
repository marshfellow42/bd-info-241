import os
import sqlite3
import sys
import platform
import uvicorn
from fastapi import FastAPI

def prerequisites():
    # Global variable to check the operational system used
    # Though it'll only used a few times
    # I believe it won't have this much of a performance boost in general, but I believe it would be a little better
    operational_system = platform.system()

    # A variable that has all the necessary imports that aren't native in Python, needing to be installed separately
    required_modules = ["fastapi", "uvicorn"]

    # Check if the imports have been imported
    missing_modules = [module for module in required_modules if module not in sys.modules]

    if missing_modules:
        if (operational_system == "Linux"):
            if ("arch" in platform.platform()):
                os.system("sudo pacman -Syu " + " ".join("python-" + mod for mod in missing_modules) + " --noconfirm --ask=4")
            elif ("Ubuntu" in platform.version()):
                os.system("sudo apt install " + " ".join("python3-" + mod for mod in missing_modules) + " -y")
            sys.exit()
        elif (operational_system == "Windows"):
            os.system("pip install " + " ".join(missing_modules) + " -y")
            sys.exit()

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

prerequisites()

# Inicia o servidor FastAPI
os.chdir(script_dir)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)