# Atividade-09

Usar as informações definidas na Avaliação-08 e o prompt da aula do dia 09-09-2024.

Executar o programa Python no ambiente do Play with Docker incluindo a seguinte funcionalidade:

Ler todos os registros da tabela `TB_ALUNOS` e mostrar o status de Aprovação. Usando a seguinte lógica:

- Se o numero de faltas for maior ou igual a 20 setar o atributo Aprovado_SN com FALSO (REPROVADO);
- Se a média Aritmética de N1 e N2 for < 6.0 setar o atributo Aprovado_SN com FALSO (REPROVADO);

Antes de executar o arquivo Python, você precisa baixar um "driver" para o Python:

```bash
pip install mysql-connector-python
```

O código Python para rodar esse registro é esse:

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
  id INT AUTO_INCREMENT NOT NULL,
  nome TEXT,
  nota_N1 INT,
  nota_N2 INT,
  media FLOAT,
  faltas INT,
  Aprovado_SN BOOLEAN,
  PRIMARY KEY (id)
);""")

mycursor.executemany('INSERT INTO TB_ALUNOS (nome, nota_N1, nota_N2, faltas) VALUES (%s, %s, %s, %s);', [
    ("Leandro", 8, 1, 20),
    ("Ana Lívia", 10, 10, 0),
    ("José Maia", 10, 2, 1),
    ("Kelwin", 9, 0, 30)
])

mydb.commit()

mycursor.execute("SELECT * FROM TB_ALUNOS")
meuresultado = mycursor.fetchall()

for item in meuresultado:
    id, nome, nota_N1, nota_N2, media, faltas, aprovado_sn = item

    media_parcial = (2 * nota_N1 + 3 * nota_N2) / 5

    if media_parcial < 6.0 or faltas >= 20:
        aprovado_sn = False
    else:
        aprovado_sn = True

    mycursor.execute('UPDATE TB_ALUNOS SET Aprovado_SN = %s, media = %s WHERE id = %s;', (aprovado_sn, media_parcial, id))

mydb.commit()

mycursor.execute("SELECT * FROM TB_ALUNOS")
meuresultado = mycursor.fetchall()

for item in meuresultado:
    id, nome, nota_N1, nota_N2, media, faltas, aprovado_sn = item

    status = "APROVADO" if aprovado_sn else "REPROVADO"
    
    print(f"Aluno: {nome}, Nota N1: {nota_N1}, Nota N2: {nota_N2}, Media: {media}, Faltas: {faltas}, Status: {status}")

    print()

mycursor.close()
mydb.close()
```

## Como executar o código Python no [Play with Docker](https://labs.play-with-docker.com/)?

Para executar o código Python no Play with Docker, você primeiro precisa rodar o script `.sh`, pois esse script contém os pré-requisitos para você rodar o código sem ter erros.

Para rodar esse script, você precisa executar esses comandos no terminal:

```bash
git clone https://github.com/marshfellow42/bd-info-241.git

chmod +x bd-info-241/atividades/atividade-09/rode_isso_no_shell.sh

./bd-info-241/atividades/atividade-09/rode_isso_no_shell.sh
```
