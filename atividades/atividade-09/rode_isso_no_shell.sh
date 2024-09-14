#!/bin/bash

apk update

apk upgrade

cat <<EOF > docker-compose.yml
version: '3.8'

services:
  mysql:
    image: mysql:8.0
    container_name: mysql_container
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: mydatabase
      MYSQL_USER: myuser
      MYSQL_PASSWORD: mypassword
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "3306:3306"

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: phpmyadmin_container
    environment:
      PMA_HOST: mysql
      PMA_PORT: 3306
      PMA_USER: root
      PMA_PASSWORD: rootpassword
    ports:
      - "8080:80"
    depends_on:
      - mysql

volumes:
  mysql_data:
EOF

echo

# Esse while True serve para só progredir quando o usuário colocar o login dele corretamente, caso contrário, o script inteiro não irá rodar pela falta de dependências necessárias

# $? armazena o código de saída do último comando executado
# 0 indica que o comando foi bem-sucedido
# Qualquer valor diferente de 0 indica que houve um erro
# A comparação [-eq] verifica se $? "é igual a" 0
# Se for igual a 0, significa que o último comando executou com sucesso

# Ou seja, ele verifica se o último comando foi bem-sucedido (exit status 0)
while true; do
    docker login
    if [ $? -eq 0 ]; then
        break
    else
        echo
    fi
done

echo

docker-compose up -d

echo

pip install mysql-connector-python

echo

# É o equivalente a um sleep 60, só que mais bonito
# Esse sleep 60, é necessário pois após o MySQL ser instalado pelo Docker Compose, ele ainda precisa de um tempo extra para poder fazer as finalizações dele
# E se o script executar tudo muito rápido, ele basicamente não roda nada no MySQL

# Esse for loop faz basicamente um loop 40 vezes, e nessas 40 vezes ele adiciona um sleep 0.5
# Ou seja, (0,5 * 3) * 40 = 60s = 1min
show_progress() {
    for i in {1..40}; do
        echo -ne "Iniciando o servidor MySQL.   \r"
        sleep 0.5
        echo -ne "Iniciando o servidor MySQL..  \r"
        sleep 0.5
        echo -ne "Iniciando o servidor MySQL... \r"
        sleep 0.5
        echo -ne "\r"
    done
}

show_progress

echo

echo "O servidor MySQL foi iniciado!"

echo

cat <<EOF > arquivo.py
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
EOF

# Esse sleep é desnecessário e perde o tempo de todo mundo, mas eu achei interessante colocar para o usuário se preparar para vir uma porrada de informação do banco de dados de uma vez só
sleep 1

python arquivo.py