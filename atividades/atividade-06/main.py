from fastapi import FastAPI, HTTPException
import sqlite3
import os

app = FastAPI()

# Caminho para o banco de dados SQLite
script_dir = os.path.realpath(os.path.dirname(__file__))
db_path = os.path.join(script_dir, 'dbalunos.db')

def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.post("/criar_aluno/")
def criar_aluno(aluno: str = None,  endereco: str = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO TB_ALUNO (aluno, endereco) VALUES (?, ?)', (aluno, endereco))
    conn.commit()
    conn.close()
    return {"message": "Aluno criado com sucesso"}

@app.get("/listar_alunos/")
def listar_alunos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TB_ALUNO')
    alunos = cursor.fetchall()
    conn.close()
    return {"alunos": [dict(row) for row in alunos]}

@app.get("/listar_um_aluno/{id}")
def listar_um_aluno(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TB_ALUNO WHERE id = ?', (id,))
    aluno = cursor.fetchone()
    conn.close()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return dict(aluno)

@app.put("/atualizar_aluno/{id}")
def atualizar_aluno(id: int, aluno: str = None,  endereco: str = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE TB_ALUNO SET aluno = ?, endereco = ? WHERE id = ?', (aluno, endereco, id))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"message": "Aluno atualizado com sucesso"}

@app.delete("/excluir_aluno/{id}")
def excluir_aluno(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM TB_ALUNO WHERE id = ?', (id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    cursor.execute('SELECT COUNT(*) FROM TB_ALUNO')
    row_count = cursor.fetchone()[0]

    # Resetar a sequência do ID caso não exista nenhum aluno
    # Para evitar a gambiarra do Arthur de colocar o ID junto com atualizar_aluno por causa disso
    if row_count == 0:
        cursor.execute('''
            DELETE FROM sqlite_sequence
            WHERE name = 'TB_ALUNO'
        ''')
        conn.commit()

    conn.close()
    return {"message": "Aluno excluído com sucesso"}
