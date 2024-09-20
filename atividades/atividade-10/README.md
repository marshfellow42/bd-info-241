# Atividade-10

## Questão da atividade

Crie um Banco de Dados envolvendo quatro tabelas. Uma tabela é um Cadastro (por exemplo `TB_ALUNO`), uma outra tabela é cadastro (por exemplo `TB_DISCIPLINA`) e uma outra também é cadastro (por `TB_PROFESSOR`). A quarta tabela `Matricula` se relaciona com as tabelas Aluno, Professor e Disciplina. Na tabela Matricula existirão chaves estrangeiras para Aluno, Professor e Disciplina. na tabela Matricula existirão atributos com as notas N1, N2 e Faltas. Criar instruções SQL com CRUD para as 4 tabelas. Implementar um código Python para ler a tabela Matricula e listar o status de aprovação dos alunos Matriculados.

Criar scripts sql para para prova Prática
1) Listar todos os aluno reprovados. Nome do Aluno, Nome da Disciplina, Nome do Professor, N1,N2,Média,Faltas, Status da reprovação("`Reprovado por Média`", "`Reprovado por Falta`") 
2) Listar todos os alunos aprovados. Nome Aluno, Nome da Disciplina, Nome do Professor, N1,N2,Média,Faltas, Status da reprovação("`Aprovado por Média`"); 
3) Listar a Quantidade de alunos aprovados;
4) Listar a Quantidade de alunos reprovados;

Antes de executar o arquivo `.py`, você precisa baixar um "driver de banco de dados" para o Python:

```bash
pip install mysql-connector-python
```

O código Python para rodar criar as tabelas no banco de dados é esse:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myuser",
  password="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_ALUNOS (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome TEXT
);""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_PROFESSOR (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome TEXT
);""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_DISCIPLINA (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome TEXT
);""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS Matricula (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_aluno INT,
    nome_professor INT,
    disciplina INT,
    nota_N1 FLOAT,
    nota_N2 FLOAT,
    faltas INT,
    Aprovado_SN BOOLEAN,
    FOREIGN KEY (nome_aluno) REFERENCES TB_ALUNOS(id),
    FOREIGN KEY (nome_professor) REFERENCES TB_PROFESSOR(id),
    FOREIGN KEY (disciplina) REFERENCES TB_DISCIPLINA(id)
);""")

mydb.commit()

print("TB_ALUNOS foi criado")
print("TB_PROFESSORES foi criado")
print("TB_DISCIPLINA foi criado")
print("Matricula foi criado")

mycursor.close()
mydb.close()
```

---

Agora, para um CRUD completo, onde o usuário pode interagir com o banco de dados

Você precisa também baixar uma biblioteca para o sistema de cores em Python:

```bash
pip install mysql-connector-python colorama
```

O código Python é [esse](https://github.com/marshfellow42/bd-info-241/blob/main/atividades/atividade-10/script.py)

## Como executar o código Python no [Play with Docker](https://labs.play-with-docker.com/)?

Para executar o código Python no Play with Docker, você primeiro precisa rodar o `script`, pois esse script contém os pré-requisitos para você rodar o código sem ter erros.

Para rodar esse script, você precisa executar esses comandos no terminal:

```bash
git clone https://github.com/marshfellow42/bd-info-241.git

cd bd-info-241/atividades/atividade-10

chmod +x rode_isso_no_shell

./rode_isso_no_shell
```
