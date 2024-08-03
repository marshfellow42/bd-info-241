from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()

# Caminho para o banco de dados SQLite
script_dir = os.path.realpath(os.path.dirname(__file__))
db_path = os.path.join(script_dir, 'dbalunos.db')

# Modelo Pydantic para validar os dados de entrada
class Aluno(BaseModel):
    aluno: str
    endereco: str

def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.post("/criar_aluno/")
def criar_aluno(aluno: Aluno):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO TB_ALUNO (aluno, endereco) VALUES (?, ?)', (aluno.aluno, aluno.endereco))
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
def atualizar_aluno(id: int, aluno: Aluno):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE TB_ALUNO SET aluno = ?, endereco = ? WHERE id = ?', (aluno.aluno, aluno.endereco, id))
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
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"message": "Aluno excluído com sucesso"}
