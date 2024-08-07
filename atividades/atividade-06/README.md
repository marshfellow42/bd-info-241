# Atividade-06
Desenvolver um Backend Python que usa FASTAPI 

Como um programador Python, crie uma aplicação backend que usa o framework FASTAPI seguindo os seguintes passos:

1) Crie um banco de dados SQLITE3 com o nome dbalunos.db.

2) Crie uma entidade aluno que será persistida em uma tabela TB_ALUNO com os seguintes campos:
<br>
`id` chave primária do tipo inteiro com autoincremento;
<br>
`aluno_nome` do tipo string com tamanho 50;
<br>
`endereço` do tipo string com tamanho 100;

3) Crie os seguintes endpoints FASTAPI abaixo descritos:
<br> 
a) criar_aluno grava dados de um objeto aluno na tabela TB_ALUNO;
<br>
b) listar_alunos ler todos os registros da tabela TB_ALUNO;
<br>
c) listar_um_aluno ler um registro da tabela TB_ALUNO a partir do campo id;
<br> 
d) atualizar_aluno atualiza um registro da tabela TB_ALUNO a partir de um campo id e dos dados de uma entidade aluno;
<br>
e) excluir_aluno exclui um registro da tabela TB_ALUNO a partir de um campo id e dos dados de uma entidade aluno;

---

## Comandos para rodar a API

Rode esses commandos no `cmd` caso você esteja usando Windows. No Powershell não funciona

E rode o programa `rode_isso_primeiro.py` como o arquivo principal, para assegurar que tudo funcione corretamente

### Criar aluno

```bash
curl -X POST "http://127.0.0.1:8000/criar_aluno/" -H "Content-Type: application/json" -d "{\"aluno\": \"João da Silva\", \"endereco\": \"Rua das Flores, 123\"}"
```

### Listar todos os alunos

```bash
curl -X GET "http://127.0.0.1:8000/listar_alunos/"
```

### Listar um Aluno específico

```bash
curl -X GET "http://127.0.0.1:8000/listar_um_aluno/1"
```

<p><small>Certifique-se de que o ID do aluno é um número válido.</small></p>

### Atualizar um Aluno

```bash
curl -X PUT "http://127.0.0.1:8000/atualizar_aluno/1" -H "Content-Type: application/json" -d "{\"aluno\": \"João da Silva Júnior\", \"endereco\": \"Rua das Flores, 456\"}"
```

### Excluir um Aluno

```bash
curl -X DELETE "http://127.0.0.1:8000/excluir_aluno/1"
```