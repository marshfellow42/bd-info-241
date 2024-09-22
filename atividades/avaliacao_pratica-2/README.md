# Avaliação Prática 2

## Requesitos da Avaliação

Criar scripts sql para para prova Prática
1) Listar todos os aluno reprovados. Nome do Aluno, Nome da Disciplina, Nome do Professor, N1, N2, Média, Faltas, Status da reprovação("`Reprovado por Média`", "`Reprovado por Falta`") 
2) Listar todos os alunos aprovados. Nome Aluno, Nome da Disciplina, Nome do Professor, N1, N2, Média, Faltas, Status da reprovação("`Aprovado por Média`"); 
3) Listar a Quantidade de alunos aprovados;
4) Listar a Quantidade de alunos reprovados;

Ao invés de criar arquivos SQL pré-fabricados, eu deixei isso a cargo do usuário por meio do arquivo Python. Mas lá também tem uma forma de fazer a avaliação inteira apertando só dois botões.

Antes de executar o arquivo `.py`, você precisa baixar um "driver de banco de dados" para o Python:

Você precisa também baixar uma biblioteca para o sistema de cores em Python:

```bash
pip install mysql-connector-python colorama
```

Pois fica bem difícil reconhecer se o resultado foi positivo ou negativo em uma linha branca.

O código Python é [esse](https://github.com/marshfellow42/bd-info-241/blob/main/atividades/avaliacao_pratica-2/script.py)

## Como executar o código Python no [Play with Docker](https://labs.play-with-docker.com/)?

Para executar o código Python no Play with Docker, você primeiro precisa rodar o `script`, pois esse script contém os pré-requisitos para você rodar o código sem ter erros.

Para rodar esse script, você precisa executar esses comandos no terminal:

```bash
git clone https://github.com/marshfellow42/bd-info-241.git

cd bd-info-241/atividades/avaliacao_pratica-2

chmod +x rode_isso_no_shell

./rode_isso_no_shell
```
