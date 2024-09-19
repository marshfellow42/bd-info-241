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

O código Python é esse:

```python
import mysql.connector
from colorama import *

init()

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
    id_aluno INT,
    id_professor INT,
    id_disciplina INT,
    nota_N1 FLOAT,
    nota_N2 FLOAT,
    media FLOAT,
    faltas INT,
    Aprovado_SN BOOLEAN,
    FOREIGN KEY (id_aluno) REFERENCES TB_ALUNOS(id),
    FOREIGN KEY (id_professor) REFERENCES TB_PROFESSOR(id),
    FOREIGN KEY (id_disciplina) REFERENCES TB_DISCIPLINA(id)
);""")


mydb.commit()

# Funcionalidades CRUD para geral

# Create
def create_data_on_table(tabela):
    match(tabela):
        case "TB_ALUNOS":
            nome = input("Coloque o nome do aluno: ")
            mycursor.execute("INSERT INTO TB_ALUNOS (nome) VALUES (%s);", (nome,))
            mydb.commit()
        case "TB_PROFESSOR":
            nome = input("Coloque o nome do professor: ")
            mycursor.execute("INSERT INTO TB_PROFESSOR (nome) VALUES (%s);", (nome,))
            mydb.commit()
        case "TB_DISCIPLINA":
            nome = input("Coloque o nome da disciplina: ")
            mycursor.execute("INSERT INTO TB_DISCIPLINA (nome) VALUES (%s);", (nome,))
            mydb.commit()
        case "Matricula":
            nome_aluno = input("Coloque o ID do aluno: ")
            nome_professor = input("Coloque o ID do professor: ")
            disciplina = input("Coloque o ID da disciplina: ")
            nota_N1 = float(input("Coloque a nota da N1: "))
            nota_N2 = float(input("Coloque a nota da N2: "))
            faltas = int(input("Coloque o número de faltas: "))

            media_parcial = (2 * nota_N1 + 3 * nota_N2) / 5

            if media_parcial < 6.0 or faltas >= 20:
                aprovado_sn = False
            else:
                aprovado_sn = True

            mycursor.execute("INSERT INTO Matricula (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media, faltas, Aprovado_SN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (nome_aluno, nome_professor, disciplina, nota_N1, nota_N2, media_parcial, faltas, aprovado_sn))
            mydb.commit()

# Read
def read_data_on_table(tabela):
    mycursor.execute(f"SELECT * FROM {tabela}")
    meuresultado = mycursor.fetchall()

    match(tabela):
        case "TB_ALUNOS":
            for item in meuresultado:
                id, nome = item
                print(f"ID: {id}, ",
                    f"Aluno: {nome}")
        case "TB_PROFESSOR":
            for item in meuresultado:
                id, nome = item
                print(f"ID: {id}, ",
                    f"Professor: {nome}")
        case "TB_DISCIPLINA":
            for item in meuresultado:
                id, nome = item
                print(f"ID: {id}, ",
                    f"Disciplina: {nome}")
        case "Matricula":
            for item in meuresultado:
                id, id_aluno, id_professor, disciplina, nota_N1, nota_N2, media, faltas, aprovado_sn = item

                mycursor.execute(f"SELECT nome FROM TB_ALUNOS WHERE id = {id_aluno}")
                nome_aluno = mycursor.fetchone()[0]

                mycursor.execute(f"SELECT nome FROM TB_PROFESSOR WHERE id = {id_professor}")
                nome_professor = mycursor.fetchone()[0]

                mycursor.execute(f"SELECT nome FROM TB_DISCIPLINA WHERE id = {disciplina}")
                nome_disciplina = mycursor.fetchone()[0]

                media_parcial = (2 * nota_N1 + 3 * nota_N2) / 5

                if media_parcial < 6.0 or faltas >= 20:
                    aprovado_sn = False
                else:
                    aprovado_sn = True

                # Nome do status após ser aprovado
                if aprovado_sn:
                    status = "Aprovado por Média"
                elif (not aprovado_sn) and (faltas >= 20) and (media_parcial < 6.0):
                    status = "Reprovado por Falta e por Média"
                elif (not aprovado_sn) and (faltas >= 20):
                    status = "Reprovado por Falta"
                elif (not aprovado_sn) and (media_parcial < 6.0):
                    status = "Reprovado por Média"

                # Cor das Faltas
                if faltas < 10:
                    faltas_color = Fore.GREEN
                elif faltas < 20:
                    faltas_color = Fore.YELLOW
                else:
                    faltas_color = Fore.RED

                # Cor dos Status
                if aprovado_sn:
                    status_color = Fore.GREEN  
                else:
                    status_color = Fore.RED

                # Cor da Nota N1
                if nota_N1 <= 5:
                    nota_n1_color = Fore.RED
                elif nota_N1 <= 9:
                    nota_n1_color = Fore.YELLOW
                else:
                    nota_n1_color = Fore.GREEN

                # Cor da Nota N2
                if nota_N2 <= 5:
                    nota_n2_color = Fore.RED
                elif nota_N2 <= 9:
                    nota_n2_color = Fore.YELLOW
                else:
                    nota_n2_color = Fore.GREEN

                # Cor da media
                if nota_N2 <= 5:
                    media_color = Fore.RED
                elif nota_N2 <= 9:
                    media_color = Fore.YELLOW
                else:
                    media_color = Fore.GREEN

                # Cor da Disciplina
                match(nome_disciplina):
                    case "PHP":
                        disciplina_color = Fore.LIGHTBLUE_EX
                    case _:
                        disciplina_color = ""

                # Eu poderia colocar esses IFs acima como forma de ternário na parte onde tem as suas respectivas variáveis abaixo
                # Mas ternário em Python é muito feio e fica bem difícil de entender para onde cada coisa vai
                # Exemplo: f"Faltas:{Fore.GREEN if faltas < 10 else Fore.YELLOW if faltas <= 20 else Fore.RED} {faltas} {Fore.RESET}"
                print(f"ID: {id}, "
                    f"Aluno: {nome_aluno}, "
                    f"Professor: {nome_professor}, "
                    f"Disciplina:{disciplina_color} {nome_disciplina}{Fore.RESET}, "
                    f"Nota N1:{nota_n1_color} {nota_N1}{Fore.RESET}, "
                    f"Nota N2:{nota_n2_color} {nota_N2}{Fore.RESET}, "
                    f"Media:{media_color} {media_parcial}{Fore.RESET}, "
                    f"Faltas:{faltas_color} {faltas}{Fore.RESET}, "
                    f"Status:{status_color} {status}{Style.RESET_ALL}")

# Update
def update_data_on_table(tabela):
    id = int(input("Qual o id da linha que você deseja atualizar: "))
    match(tabela):
        case "TB_ALUNOS":
            nome = input("Coloque o nome do aluno: ")
            mycursor.execute(f"UPDATE TB_ALUNOS SET nome = %s WHERE id = %s;", (nome, id))
            mydb.commit()
        case "TB_PROFESSOR":
            nome = input("Coloque o nome do professor: ")
            mycursor.execute(f"UPDATE TB_PROFESSOR SET nome = %s WHERE id = %s;", (nome, id))
            mydb.commit()
        case "TB_DISCIPLINA":
            nome = input("Coloque o nome da disciplina: ")
            mycursor.execute(f"UPDATE TB_DISCIPLINA SET nome = %s WHERE id = %s;", (nome, id))
            mydb.commit()
        case "Matricula":
            id_aluno = input("Coloque o ID do aluno: ")
            id_professor = input("Coloque o ID do professor: ")
            id_disciplina = input("Coloque o ID da disciplina: ")
            nota_N1 = float(input("Coloque a nota da N1: "))
            nota_N2 = float(input("Coloque a nota da N2: "))
            faltas = int(input("Coloque o número de faltas: "))

            media_parcial = (2 * nota_N1 + 3 * nota_N2) / 5

            if media_parcial < 6.0 or faltas >= 20:
                aprovado_sn = False
            else:
                aprovado_sn = True

            mycursor.execute(f"UPDATE Matricula SET id_aluno = %s, id_professor = %s, id_disciplina = %s, nota_N1 = %s, nota_N2 = %s, media = %s, faltas = %s, Aprovado_SN = %s WHERE id = %s;", (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media_parcial, faltas, aprovado_sn, id))
            mydb.commit()

# Delete
def delete_data_on_table(tabela):
    id = int(input("Qual o id da linha que você deseja deletar: "))
    mycursor.execute(f"DELETE FROM {tabela} WHERE id = %s", (id,))
    mydb.commit()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Input do usuário

while True:

    print("""1 - Colocar os dados manualmente no banco de dados
2 - Ver um preview do resultado final
3 - Listar todos os aluno aprovados
4 - Listar todos os alunos reprovados
5 - Listar a quantidade de alunos aprovados
6 - Listar a quantidade de alunos reprovados
7 - Sair
""")

    escolha_usuario = int(input("O que você deseja fazer? "))

    print()

    match(escolha_usuario):
        case 1:
            while True:
                print("Escolha uma função abaixo")

                print()

                print("""1 - Criar um dado novo em uma tabela (TB_ALUNOS, TB_PROFESSOR, TB_DISCIPLINA, Matricula)
2 - Ler todos os dados na tabela (TB_ALUNOS, TB_PROFESSOR, TB_DISCIPLINA, Matricula)
3 - Atualizar um dado na tabela (TB_ALUNOS, TB_PROFESSOR, TB_DISCIPLINA, Matricula)
4 - Deletar um dado na tabela (TB_ALUNOS, TB_PROFESSOR, TB_DISCIPLINA, Matricula)
5 - Sair
""")

                escolha = int(input("O que você deseja fazer? "))

                if escolha < 5:
                    while True:

                        print()

                        print("""Escolha uma tabela abaixo
1 - TB_ALUNOS
2 - TB_PROFESSOR
3 - TB_DISCIPLINA
4 - Matricula
""")

                        escolha_tabela = int(input("O que você deseja fazer? "))

                        if escolha_tabela > 4 or escolha_tabela < 1:
                            print("Escolha um número entre 1 e 4")
                            continue
                        else:
                            match(escolha_tabela):
                                case 1:
                                    nome_tabela = "TB_ALUNOS"
                                case 2:
                                    nome_tabela = "TB_PROFESSOR"
                                case 3:
                                    nome_tabela = "TB_DISCIPLINA"
                                case 4:
                                    nome_tabela = "Matricula"

                        print()   
                        break

                    match(escolha):
                        case 1:
                            create_data_on_table(nome_tabela)
                        case 2:
                            read_data_on_table(nome_tabela)
                        case 3:
                            update_data_on_table(nome_tabela)
                        case 4:
                            delete_data_on_table(nome_tabela)
                        case 5:
                            break

                    print()

                elif escolha > 5:
                    print("Escolha um número entre 1 e 5")
                    continue
                else:
                    break
        case 2:
            mycursor.execute("INSERT INTO TB_ALUNOS (nome) VALUES (%s);", ("Leandro",))
            mydb.commit()
            id_aluno = mycursor.lastrowid

            mycursor.execute("INSERT INTO TB_PROFESSOR (nome) VALUES (%s);", ("Anthony",))
            mydb.commit()
            id_professor = mycursor.lastrowid

            mycursor.execute("INSERT INTO TB_DISCIPLINA (nome) VALUES (%s);", ("PHP",))
            mydb.commit()
            id_disciplina = mycursor.lastrowid

            nota_N1 = 5.0
            nota_N2 = 7.0
            faltas = 9
            media_parcial = (2 * nota_N1 + 3 * nota_N2) / 5

            if media_parcial < 6.0 or faltas >= 20:
                aprovado_sn = False
            else:
                aprovado_sn = True

            mycursor.execute("INSERT INTO Matricula (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media, faltas, Aprovado_SN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media_parcial, faltas, aprovado_sn))
            mydb.commit()
            id_matricula = mycursor.lastrowid

            read_data_on_table("Matricula")

            print()
            input("Pressione Enter para continuar")

            mycursor.execute("DELETE FROM Matricula WHERE id = %s", (id_matricula,))
            mydb.commit()

            mycursor.execute("DELETE FROM TB_ALUNOS WHERE id = %s", (id_aluno,))
            mydb.commit()

            mycursor.execute("DELETE FROM TB_PROFESSOR WHERE id = %s", (id_professor,))
            mydb.commit()

            mycursor.execute("DELETE FROM TB_DISCIPLINA WHERE id = %s", (id_disciplina,))
            mydb.commit()

            mycursor.execute("ALTER TABLE TB_ALUNOS AUTO_INCREMENT = 1")
            mydb.commit()

            mycursor.execute("ALTER TABLE TB_PROFESSOR AUTO_INCREMENT = 1")
            mydb.commit()

            mycursor.execute("ALTER TABLE TB_DISCIPLINA AUTO_INCREMENT = 1")
            mydb.commit()

            mycursor.execute("ALTER TABLE Matricula AUTO_INCREMENT = 1")
            mydb.commit()
        
        case 3: 
            mycursor.execute("SELECT * FROM Matricula WHERE Aprovado_sn = 1")
            meuresultado = mycursor.fetchall()

            if not meuresultado:
                print("Nenhum aluno foi aprovado.")
            else:
                for item in meuresultado:
                    id, id_aluno, id_professor, disciplina, nota_N1, nota_N2, media, faltas, aprovado_sn = item

                    mycursor.execute(f"SELECT nome FROM TB_ALUNOS WHERE id = {id_aluno}")
                    nome_aluno = mycursor.fetchone()[0]

                    mycursor.execute(f"SELECT nome FROM TB_PROFESSOR WHERE id = {id_professor}")
                    nome_professor = mycursor.fetchone()[0]

                    mycursor.execute(f"SELECT nome FROM TB_DISCIPLINA WHERE id = {disciplina}")
                    nome_disciplina = mycursor.fetchone()[0]

                    media_parcial = (2 * nota_N1 + 3 * nota_N2) / 5

                    if aprovado_sn:
                        status = "Aprovado por Média"
                    elif (not aprovado_sn) and (faltas >= 20) and (media_parcial < 6.0):
                        status = "Reprovado por Falta e por Média"
                    elif (not aprovado_sn) and (faltas >= 20):
                        status = "Reprovado por Falta"
                    elif (not aprovado_sn) and (media_parcial < 6.0):
                        status = "Reprovado por Média"

                    # Cor das Faltas
                    if faltas < 10:
                        faltas_color = Fore.GREEN
                    elif faltas < 20:
                        faltas_color = Fore.YELLOW
                    else:
                        faltas_color = Fore.RED

                    # Cor dos Status
                    if aprovado_sn:
                        status_color = Fore.GREEN  
                    else:
                        status_color = Fore.RED

                    # Cor da Nota N1
                    if nota_N1 <= 5:
                        nota_n1_color = Fore.RED
                    elif nota_N1 <= 9:
                        nota_n1_color = Fore.YELLOW
                    else:
                        nota_n1_color = Fore.GREEN

                    # Cor da Nota N2
                    if nota_N2 <= 5:
                        nota_n2_color = Fore.RED
                    elif nota_N2 <= 9:
                        nota_n2_color = Fore.YELLOW
                    else:
                        nota_n2_color = Fore.GREEN

                    # Cor da media
                    if nota_N2 <= 5:
                        media_color = Fore.RED
                    elif nota_N2 <= 9:
                        media_color = Fore.YELLOW
                    else:
                        media_color = Fore.GREEN

                    # Cor da Disciplina
                    match(nome_disciplina):
                        case "PHP":
                            disciplina_color = Fore.LIGHTBLUE_EX
                        case _:
                            disciplina_color = ""
                            
                    print(f"ID: {id}, "
                        f"Aluno: {nome_aluno}, "
                        f"Professor: {nome_professor}, "
                        f"Disciplina:{disciplina_color} {nome_disciplina}{Fore.RESET}, "
                        f"Nota N1:{nota_n1_color} {nota_N1}{Fore.RESET}, "
                        f"Nota N2:{nota_n2_color} {nota_N2}{Fore.RESET}, "
                        f"Media:{media_color} {media_parcial}{Fore.RESET}, "
                        f"Faltas:{faltas_color} {faltas}{Fore.RESET}, "
                        f"Status:{status_color} {status}{Style.RESET_ALL}")

        case 4:
            mycursor.execute(f"SELECT * FROM Matricula WHERE Aprovado_sn = 0")
            meuresultado = mycursor.fetchall()

            if not meuresultado:
                print("Nenhum aluno foi reprovado.")
            else:
                for item in meuresultado:
                    id, id_aluno, id_professor, disciplina, nota_N1, nota_N2, media, faltas, aprovado_sn = item

                    mycursor.execute(f"SELECT nome FROM TB_ALUNOS WHERE id = {id_aluno}")
                    nome_aluno = mycursor.fetchone()[0]

                    mycursor.execute(f"SELECT nome FROM TB_PROFESSOR WHERE id = {id_professor}")
                    nome_professor = mycursor.fetchone()[0]

                    mycursor.execute(f"SELECT nome FROM TB_DISCIPLINA WHERE id = {disciplina}")
                    nome_disciplina = mycursor.fetchone()[0]

                    media_parcial = (2 * nota_N1 + 3 * nota_N2) / 5

                    if aprovado_sn:
                        status = "Aprovado por Média"
                    elif (not aprovado_sn) and (faltas >= 20) and (media_parcial < 6.0):
                        status = "Reprovado por Falta e por Média"
                    elif (not aprovado_sn) and (faltas >= 20):
                        status = "Reprovado por Falta"
                    elif (not aprovado_sn) and (media_parcial < 6.0):
                        status = "Reprovado por Média"

                    # Cor das Faltas
                    if faltas < 10:
                        faltas_color = Fore.GREEN
                    elif faltas < 20:
                        faltas_color = Fore.YELLOW
                    else:
                        faltas_color = Fore.RED

                    # Cor dos Status
                    if aprovado_sn:
                        status_color = Fore.GREEN  
                    else:
                        status_color = Fore.RED

                    # Cor da Nota N1
                    if nota_N1 <= 5:
                        nota_n1_color = Fore.RED
                    elif nota_N1 <= 9:
                        nota_n1_color = Fore.YELLOW
                    else:
                        nota_n1_color = Fore.GREEN

                    # Cor da Nota N2
                    if nota_N2 <= 5:
                        nota_n2_color = Fore.RED
                    elif nota_N2 <= 9:
                        nota_n2_color = Fore.YELLOW
                    else:
                        nota_n2_color = Fore.GREEN

                    # Cor da media
                    if nota_N2 <= 5:
                        media_color = Fore.RED
                    elif nota_N2 <= 9:
                        media_color = Fore.YELLOW
                    else:
                        media_color = Fore.GREEN

                    # Cor da Disciplina
                    match(nome_disciplina):
                        case "PHP":
                            disciplina_color = Fore.LIGHTBLUE_EX
                        case _:
                            disciplina_color = ""
                            
                    print(f"ID: {id}, "
                        f"Aluno: {nome_aluno}, "
                        f"Professor: {nome_professor}, "
                        f"Disciplina:{disciplina_color} {nome_disciplina}{Fore.RESET}, "
                        f"Nota N1:{nota_n1_color} {nota_N1}{Fore.RESET}, "
                        f"Nota N2:{nota_n2_color} {nota_N2}{Fore.RESET}, "
                        f"Media:{media_color} {media_parcial}{Fore.RESET}, "
                        f"Faltas:{faltas_color} {faltas}{Fore.RESET}, "
                        f"Status:{status_color} {status}{Style.RESET_ALL}")

        case 5:
            mycursor.execute(f"SELECT * FROM Matricula WHERE Aprovado_sn = 1")
            meuresultado = mycursor.fetchall()

            n_aprovado = 0

            for item in meuresultado:
                n_aprovado += 1

            print("Número de aprovados: " + str(n_aprovado))

        case 6:
            mycursor.execute(f"SELECT * FROM Matricula WHERE Aprovado_sn = 0")
            meuresultado = mycursor.fetchall()

            n_reprovado = 0

            for item in meuresultado:
                n_reprovado += 1

            print("Número de reprovados: " + str(n_reprovado))

        case 7:
            break

    print()

mycursor.close()
mydb.close()
```

## Como executar o código Python no [Play with Docker](https://labs.play-with-docker.com/)?

Para executar o código Python no Play with Docker, você primeiro precisa rodar o `script`, pois esse script contém os pré-requisitos para você rodar o código sem ter erros.

Para rodar esse script, você precisa executar esses comandos no terminal:

```bash
git clone https://github.com/marshfellow42/bd-info-241.git

chmod +x bd-info-241/atividades/atividade-10/rode_isso_no_shell

./bd-info-241/atividades/atividade-10/rode_isso_no_shell
```
