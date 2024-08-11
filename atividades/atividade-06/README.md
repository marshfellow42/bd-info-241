# Atividade-06

Desenvolver um Backend Python que usa FASTAPI

Como um programador Python, crie uma aplicação backend que usa o framework FASTAPI seguindo os seguintes passos:

1. Crie um banco de dados SQLITE3 com o nome `dbalunos.db`.

2. Crie uma entidade `aluno` que será persistida em uma tabela `TB_ALUNO` com os seguintes campos:
    - `id`: chave primária do tipo inteiro com autoincremento;
    - `aluno_nome`: do tipo string com tamanho 50;
    - `endereco`: do tipo string com tamanho 100;

3. Crie os seguintes endpoints FASTAPI abaixo descritos:
    - `criar_aluno`: grava dados de um objeto aluno na tabela `TB_ALUNO`;
    - `listar_alunos`: lê todos os registros da tabela `TB_ALUNO`;
    - `listar_um_aluno`: lê um registro da tabela `TB_ALUNO` a partir do campo `id`;
    - `atualizar_aluno`: atualiza um registro da tabela `TB_ALUNO` a partir de um campo `id` e dos dados de uma entidade aluno;
    - `excluir_aluno`: exclui um registro da tabela `TB_ALUNO` a partir de um campo `id` e dos dados de uma entidade aluno;

---

## Comandos para rodar a API

Rode esses commandos no `cmd` caso você esteja usando Windows. No Powershell não funciona

E rode o programa `rode_isso_primeiro.py` como o arquivo principal, para assegurar que tudo funcione corretamente

### Criar aluno

```bash
curl -X POST "http://127.0.0.1:8000/criar_aluno/?aluno=Jo%C3%A3o%20da%20Silva&endereco=Rua%20das%20Flores%2C%20123" -H "accept: application/json" -d ""
```

<p><small>O nome do aluno e o endereço precisando ser encodados com um padrão em que a URL consiga entender</small></p>

<p><small>Esse <a href="https://emn178.github.io/online-tools/url_encode.html">website</a> permite facilitar o processo de encodar o texto para o padrão da URL</small></p>

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
curl -X PUT "http://127.0.0.1:8000/atualizar_aluno/1?aluno=Jo%C3%A3o%20da%20Silva&endereco=Rua%20das%20Flores%2C%20124" -H "accept: application/json"
```

### Excluir um Aluno

```bash
curl -X DELETE "http://127.0.0.1:8000/excluir_aluno/1"
```
