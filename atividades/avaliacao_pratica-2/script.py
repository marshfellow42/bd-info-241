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

# Funções Reutilizáveis
def input_matricula ():
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

    return id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, faltas, media_parcial, aprovado_sn

def selecoes_tabelas(tabela, assunto_aluno, assunto_professor, assunto_disciplina):
    match (tabela):
        case "TB_ALUNOS":
            return assunto_aluno
        case "TB_PROFESSOR":
            return assunto_professor
        case "TB_DISCIPLINA":
            return assunto_disciplina

def decisao_status(aprovado_sn, faltas, media):
    # Nome do status após ser aprovado
    if aprovado_sn:
        status = "Aprovado por Média"
    elif (not aprovado_sn) and (faltas >= 20) and (media < 6.0):
        status = "Reprovado por Média e por Falta"
    elif (not aprovado_sn) and (faltas >= 20):
        status = "Reprovado por Falta"
    elif (not aprovado_sn) and (media < 6.0):
        status = "Reprovado por Média"
    
    return status

def selecao_cor(faltas, aprovado_sn, nota_N1, nota_N2, media, nome_disciplina):
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
    if nota_N1 <= 5.9:
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
    if media < 3:
        media_color = Fore.RED
    elif media >= 3 and media <= 5.9:
        media_color = Fore.YELLOW
    else:
        media_color = Fore.GREEN

    # Cor da Disciplina
    match(nome_disciplina):
        case "PHP":
            disciplina_color = Fore.LIGHTBLUE_EX
        case _:
            disciplina_color = ""

    return faltas_color, status_color, nota_n1_color, nota_n2_color, media_color, disciplina_color

def print_array_matricula(id, nome_aluno, nome_professor, nome_disciplina, nota_N1, nota_N2, media, faltas, status, disciplina_color, nota_n1_color, nota_n2_color, media_color, faltas_color, status_color):
    print(f"ID: {id}, "
        f"Aluno: {nome_aluno}, "
        f"Professor: {nome_professor}, "
        f"Disciplina:{disciplina_color} {nome_disciplina}{Fore.RESET}, "
        f"Nota N1:{nota_n1_color} {nota_N1}{Fore.RESET}, "
        f"Nota N2:{nota_n2_color} {nota_N2}{Fore.RESET}, "
        f"Media:{media_color} {media}{Fore.RESET}, "
        f"Faltas:{faltas_color} {faltas}{Fore.RESET}, "
        f"Status:{status_color} {status}{Style.RESET_ALL}")

# Funcionalidades CRUD para geral

# Create
def create_data_on_table(tabela):
    if tabela == "Matricula":
        id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, faltas, media_parcial, aprovado_sn = input_matricula()

        mycursor.execute("INSERT INTO Matricula (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media, faltas, Aprovado_SN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media_parcial, faltas, aprovado_sn))
        mydb.commit()
    else:
        assunto = selecoes_tabelas(tabela, "do aluno", "do professor(a)", "da disciplina")
        nome = input(f"Coloque o nome {assunto}: ")
        mycursor.execute(f"INSERT INTO {tabela} (nome) VALUES (%s);", (nome,))
        mydb.commit()

def read_data_on_table(tabela):
    mycursor.execute(f"SELECT * FROM {tabela}")
    meuresultado = mycursor.fetchall()

    if tabela == "Matricula":
        for item in meuresultado:
            id, id_aluno, id_professor, disciplina, nota_N1, nota_N2, media, faltas, aprovado_sn = item

            mycursor.execute(f"SELECT nome FROM TB_ALUNOS WHERE id = {id_aluno}")
            nome_aluno = mycursor.fetchone()[0]

            mycursor.execute(f"SELECT nome FROM TB_PROFESSOR WHERE id = {id_professor}")
            nome_professor = mycursor.fetchone()[0]

            mycursor.execute(f"SELECT nome FROM TB_DISCIPLINA WHERE id = {disciplina}")
            nome_disciplina = mycursor.fetchone()[0]

            status = decisao_status(aprovado_sn, faltas, media)

            faltas_color, status_color, nota_n1_color, nota_n2_color, media_color, disciplina_color = selecao_cor(faltas, aprovado_sn, nota_N1, nota_N2, media, nome_disciplina)

            print_array_matricula(id, nome_aluno, nome_professor, nome_disciplina, nota_N1, nota_N2, media, faltas, status, disciplina_color, nota_n1_color, nota_n2_color, media_color, faltas_color, status_color)
    elif tabela == "Matricula_teste":
        for item in meuresultado:
            id, id_aluno, id_professor, disciplina, nota_N1, nota_N2, media, faltas, aprovado_sn = item

            mycursor.execute(f"SELECT nome FROM TB_ALUNOS_teste WHERE id = {id_aluno}")
            nome_aluno = mycursor.fetchone()[0]

            mycursor.execute(f"SELECT nome FROM TB_PROFESSOR_teste WHERE id = {id_professor}")
            nome_professor = mycursor.fetchone()[0]

            mycursor.execute(f"SELECT nome FROM TB_DISCIPLINA_teste WHERE id = {disciplina}")
            nome_disciplina = mycursor.fetchone()[0]

            status = decisao_status(aprovado_sn, faltas, media)

            faltas_color, status_color, nota_n1_color, nota_n2_color, media_color, disciplina_color = selecao_cor(faltas, aprovado_sn, nota_N1, nota_N2, media, nome_disciplina)

            print_array_matricula(id, nome_aluno, nome_professor, nome_disciplina, nota_N1, nota_N2, media, faltas, status, disciplina_color, nota_n1_color, nota_n2_color, media_color, faltas_color, status_color)
    else:
        assunto = selecoes_tabelas(tabela, "Aluno", "Professor(a)", "Disciplina")
        for item in meuresultado:
            id, nome = item
            print(f"ID: {id}, {assunto}: {nome}")
# Update
def update_data_on_table(tabela):
    id = int(input("Qual o id da linha que você deseja atualizar: "))
    
    if tabela == "Matricula":
        id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, faltas, media_parcial, aprovado_sn = input_matricula()

        mycursor.execute(f"UPDATE Matricula SET id_aluno = %s, id_professor = %s, id_disciplina = %s, nota_N1 = %s, nota_N2 = %s, media = %s, faltas = %s, Aprovado_SN = %s WHERE id = %s;", (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media_parcial, faltas, aprovado_sn, id))
        mydb.commit()
    else:
        selecoes_tabelas(tabela, "do aluno", "do professor(a)", "da disciplina")

        nome = input(f"Coloque o nome {assunto}: ")
        mycursor.execute(f"UPDATE {tabela} SET nome = %s WHERE id = %s;", (nome, id))
        mydb.commit()

# Delete
def delete_data_on_table(tabela):
    id = int(input("Qual o id da linha que você deseja deletar: "))
    mycursor.execute(f"DELETE FROM {tabela} WHERE id = %s", (id,))
    mydb.commit()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Input do usuário

numero_saida_principal = 9
numero_saida_crud = 5
numero_saida_tabela = 5

while True:

    print(f"""1 - Fazer o CRUD manualmente no banco de dados
2 - Ver um preview do resultado final
3 - Listar todos os aluno aprovados
4 - Listar todos os alunos reprovados
5 - Listar a quantidade de alunos aprovados
6 - Listar a quantidade de alunos reprovados
7 - Fazer a avaliação inteira
8 - Excluir todos os dados de todas as tabelas
{numero_saida_principal} - Sair
""")

    escolha_usuario = int(input("O que você deseja fazer? "))

    print()

    match(escolha_usuario):
        case 1:
            while True:
                print("Escolha uma função abaixo")

                print()

                print(f"""1 - Criar um dado novo em uma tabela (TB_ALUNOS, TB_PROFESSOR, TB_DISCIPLINA, Matricula)
2 - Ler todos os dados na tabela (TB_ALUNOS, TB_PROFESSOR, TB_DISCIPLINA, Matricula)
3 - Atualizar um dado na tabela (TB_ALUNOS, TB_PROFESSOR, TB_DISCIPLINA, Matricula)
4 - Deletar um dado na tabela (TB_ALUNOS, TB_PROFESSOR, TB_DISCIPLINA, Matricula)
{numero_saida_crud} - Sair
""")

                escolha = int(input("O que você deseja fazer? "))

                if escolha != numero_saida_crud:
                    while True:

                        print()

                        print(f"""Escolha uma tabela abaixo
1 - TB_ALUNOS
2 - TB_PROFESSOR
3 - TB_DISCIPLINA
4 - Matricula
{numero_saida_tabela} - Sair
""")

                        escolha_tabela = int(input("O que você deseja fazer? "))

                        if escolha_tabela > numero_saida_tabela or escolha_tabela < 1:
                            print(f"Escolha um número entre 1 e {numero_saida_tabela}")
                            continue
                        elif escolha_tabela == numero_saida_tabela:
                            break
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

                    if escolha_tabela == numero_saida_tabela:
                        pass
                    else:
                        match(escolha):
                            case 1:
                                create_data_on_table(nome_tabela)
                            case 2:
                                read_data_on_table(nome_tabela)
                            case 3:
                                update_data_on_table(nome_tabela)
                            case 4:
                                delete_data_on_table(nome_tabela)
                            case numero_saida_crud:
                                break

                    print()

                elif escolha > numero_saida_crud or escolha < 1:
                    print(f"Escolha um número entre 1 e {numero_saida_crud}")
                    continue
                else:
                    break
        case 2:
            mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_ALUNOS_teste (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome TEXT
            );""")

            mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_PROFESSOR_teste (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome TEXT
            );""")

            mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_DISCIPLINA_teste (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome TEXT
            );""")

            mycursor.execute("""CREATE TABLE IF NOT EXISTS Matricula_teste (
                id INT PRIMARY KEY AUTO_INCREMENT,
                id_aluno INT,
                id_professor INT,
                id_disciplina INT,
                nota_N1 FLOAT,
                nota_N2 FLOAT,
                media FLOAT,
                faltas INT,
                Aprovado_SN BOOLEAN,
                FOREIGN KEY (id_aluno) REFERENCES TB_ALUNOS_teste(id),
                FOREIGN KEY (id_professor) REFERENCES TB_PROFESSOR_teste(id),
                FOREIGN KEY (id_disciplina) REFERENCES TB_DISCIPLINA_teste(id)
            );""")

            mydb.commit()

            mycursor.executemany("INSERT INTO TB_ALUNOS_teste (nome) VALUES (%s);", [("Leandro",), ("Kelwin",), ("Samuel",), ("Enzo",)])

            mycursor.executemany("INSERT INTO TB_PROFESSOR_teste (nome) VALUES (%s);", [("Anthony",), ("Ricardo Taveira",)])

            mycursor.executemany("INSERT INTO TB_DISCIPLINA_teste (nome) VALUES (%s);", [("PHP",), ("Banco de Dados",)])

            mydb.commit()

            id_aluno_array = [1, 2, 3, 4]
            id_professor_array = [1, 1, 2, 2]
            id_disciplina_array = [1, 1, 2, 2]
            notas_n1_array = [10.0, 7.0, 4.0, 3.0]
            notas_n2_array = [10.0, 8.0, 5.0, 6.0]
            faltas_array = [5, 22, 20, 13]

            for item in range(0, 4):
                id_aluno = id_aluno_array[item]
                id_professor = id_professor_array[item]
                id_disciplina = id_disciplina_array[item]
                nota_N1 = notas_n1_array[item]
                nota_N2 = notas_n2_array[item]
                faltas = faltas_array[item]

                media_parcial = (2 * nota_N1 + 3 * nota_N2) / 5

                if media_parcial < 6.0 or faltas >= 20:
                    aprovado_sn = False
                else:
                    aprovado_sn = True

                mycursor.execute("INSERT INTO Matricula_teste (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media, faltas, Aprovado_SN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media_parcial, faltas, aprovado_sn))

            mydb.commit()

            read_data_on_table("Matricula_teste")

            mycursor.execute("DROP TABLE Matricula_teste;")

            mycursor.execute("DROP TABLE TB_ALUNOS_teste;")

            mycursor.execute("DROP TABLE TB_PROFESSOR_teste;")

            mycursor.execute("DROP TABLE TB_DISCIPLINA_teste;")
            
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

                    status = decisao_status(aprovado_sn, faltas, media)
            
                    faltas_color, status_color, nota_n1_color, nota_n2_color, media_color, disciplina_color = selecao_cor(faltas, aprovado_sn, nota_N1, nota_N2, media, nome_disciplina)

                    print_array_matricula(id, nome_aluno, nome_professor, nome_disciplina, nota_N1, nota_N2, media, faltas, status, disciplina_color, nota_n1_color, nota_n2_color, media_color, faltas_color, status_color)

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

                    status = decisao_status(aprovado_sn, faltas, media)
            
                    faltas_color, status_color, nota_n1_color, nota_n2_color, media_color, disciplina_color = selecao_cor(faltas, aprovado_sn, nota_N1, nota_N2, media, nome_disciplina)

                    print_array_matricula(id, nome_aluno, nome_professor, nome_disciplina, nota_N1, nota_N2, media, faltas, status, disciplina_color, nota_n1_color, nota_n2_color, media_color, faltas_color, status_color)

        case 5:
            mycursor.execute("SELECT * FROM Matricula WHERE Aprovado_sn = 1")
            meuresultado = mycursor.fetchall()

            n_aprovado = 0

            for item in meuresultado:
                n_aprovado += 1

            print("Número de aprovados: " + str(n_aprovado))

        case 6:
            mycursor.execute("SELECT * FROM Matricula WHERE Aprovado_sn = 0")
            meuresultado = mycursor.fetchall()

            n_reprovado = 0

            for item in meuresultado:
                n_reprovado += 1

            print("Número de reprovados: " + str(n_reprovado))

        case 7:
            # Inserir os dados nas tabelas
            mycursor.executemany("INSERT INTO TB_ALUNOS (nome) VALUES (%s);", [("Leandro",), ("Kelwin",), ("Samuel",), ("Enzo",)])

            mycursor.executemany("INSERT INTO TB_PROFESSOR (nome) VALUES (%s);", [("Anthony",), ("Ricardo Taveira",)])

            mycursor.executemany("INSERT INTO TB_DISCIPLINA (nome) VALUES (%s);", [("PHP",), ("Banco de Dados",)])

            mydb.commit()
            
            id_aluno_array = [1, 2, 3, 4]
            id_professor_array = [1, 1, 2, 2]
            id_disciplina_array = [1, 1, 2, 2]
            notas_n1_array = [10.0, 7.0, 4.0, 3.0]
            notas_n2_array = [10.0, 8.0, 5.0, 6.0]
            faltas_array = [5, 22, 20, 13]

            for item in range(0, 4):
                id_aluno = id_aluno_array[item]
                id_professor = id_professor_array[item]
                id_disciplina = id_disciplina_array[item]
                nota_N1 = notas_n1_array[item]
                nota_N2 = notas_n2_array[item]
                faltas = faltas_array[item]

                media_parcial = (2 * nota_N1 + 3 * nota_N2) / 5

                if media_parcial < 6.0 or faltas >= 20:
                    aprovado_sn = False
                else:
                    aprovado_sn = True

                mycursor.execute("INSERT INTO Matricula (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media, faltas, Aprovado_SN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (id_aluno, id_professor, id_disciplina, nota_N1, nota_N2, media_parcial, faltas, aprovado_sn))

            mydb.commit()

            # Listar todos os alunos aprovados
            mycursor.execute("SELECT * FROM Matricula WHERE Aprovado_sn = 1")
            meuresultado = mycursor.fetchall()

            n_aprovado = 0

            if not meuresultado:
                print("Nenhum aluno foi aprovado.")
            else:
                for item in meuresultado:
                    n_aprovado += 1

                    id, id_aluno, id_professor, disciplina, nota_N1, nota_N2, media, faltas, aprovado_sn = item

                    mycursor.execute(f"SELECT nome FROM TB_ALUNOS WHERE id = {id_aluno}")
                    nome_aluno = mycursor.fetchone()[0]

                    mycursor.execute(f"SELECT nome FROM TB_PROFESSOR WHERE id = {id_professor}")
                    nome_professor = mycursor.fetchone()[0]

                    mycursor.execute(f"SELECT nome FROM TB_DISCIPLINA WHERE id = {disciplina}")
                    nome_disciplina = mycursor.fetchone()[0]

                    status = decisao_status(aprovado_sn, faltas, media)
            
                    faltas_color, status_color, nota_n1_color, nota_n2_color, media_color, disciplina_color = selecao_cor(faltas, aprovado_sn, nota_N1, nota_N2, media, nome_disciplina)

                    print_array_matricula(id, nome_aluno, nome_professor, nome_disciplina, nota_N1, nota_N2, media, faltas, status, disciplina_color, nota_n1_color, nota_n2_color, media_color, faltas_color, status_color)

            print()

            # Quantidade de alunos aprovados
            print("Número de aprovados: " + str(n_aprovado))

            print()

            # Listar todos os alunos reprovados
            mycursor.execute(f"SELECT * FROM Matricula WHERE Aprovado_sn = 0")
            meuresultado = mycursor.fetchall()

            n_reprovado = 0

            if not meuresultado:
                print("Nenhum aluno foi reprovado.")
            else:
                for item in meuresultado:
                    n_reprovado += 1

                    id, id_aluno, id_professor, disciplina, nota_N1, nota_N2, media, faltas, aprovado_sn = item

                    mycursor.execute(f"SELECT nome FROM TB_ALUNOS WHERE id = {id_aluno}")
                    nome_aluno = mycursor.fetchone()[0]

                    mycursor.execute(f"SELECT nome FROM TB_PROFESSOR WHERE id = {id_professor}")
                    nome_professor = mycursor.fetchone()[0]

                    mycursor.execute(f"SELECT nome FROM TB_DISCIPLINA WHERE id = {disciplina}")
                    nome_disciplina = mycursor.fetchone()[0]

                    status = decisao_status(aprovado_sn, faltas, media)
            
                    faltas_color, status_color, nota_n1_color, nota_n2_color, media_color, disciplina_color = selecao_cor(faltas, aprovado_sn, nota_N1, nota_N2, media, nome_disciplina)

                    print_array_matricula(id, nome_aluno, nome_professor, nome_disciplina, nota_N1, nota_N2, media, faltas, status, disciplina_color, nota_n1_color, nota_n2_color, media_color, faltas_color, status_color)

            print()

            # Quantidade de alunos repovados
            print("Número de reprovados: " + str(n_reprovado))

        case 8:
            while True:
                escolha_excluir = input(f"{Fore.RED}Você tem certeza? {Fore.RESET}(S/n): ").lower()
                
                if escolha_excluir == "s" or escolha_excluir == "y":

                    tabelas = ["Matricula", "TB_ALUNOS", "TB_PROFESSOR", "TB_DISCIPLINA"]

                    for item in range(len(tabelas)):
                        mycursor.execute(f"DELETE FROM {tabelas[item]};")
                        mycursor.execute(f"ALTER TABLE {tabelas[item]} AUTO_INCREMENT = 1;")
                        mydb.commit()

                    break
                elif escolha_excluir == "n":
                    break
                else:
                    print("Sim ou Não")
                    print()
                    continue
        case numero_saida_principal:
            break

    print()

mycursor.close()
mydb.close()