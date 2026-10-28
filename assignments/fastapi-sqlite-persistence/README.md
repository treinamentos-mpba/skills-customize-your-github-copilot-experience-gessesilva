# 📘 Atividade: Persistência de APIs com SQLite

## 🎯 Objetivo

Adapte a API de tarefas criada com FastAPI para persistir os dados em um banco SQLite. Pratique criação de tabelas, consultas SQL parametrizadas e operações CRUD com dados que continuam disponíveis após reiniciar o servidor.

## 📝 Tarefas

### 🛠️ Crie o banco e a tabela

#### Descrição
Complete a inicialização do SQLite no código inicial para criar a tabela `tasks` automaticamente quando a aplicação iniciar. O arquivo do banco deve ficar ao lado de `starter-code.py`.

#### Requisitos
O programa concluído deve:

- Usar o módulo `sqlite3`, incluído na biblioteca padrão do Python.
- Criar a tabela `tasks` com `id` inteiro e autoincremental, `title` obrigatório e `completed` inteiro com valor padrão `0`.
- Usar `CREATE TABLE IF NOT EXISTS` para que a inicialização possa ser executada mais de uma vez.
- Manter o endpoint `GET /health` funcionando.

### 🛠️ Persista a listagem e a criação

#### Descrição
Substitua o armazenamento temporário em memória por consultas ao SQLite para listar e criar tarefas.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks` consultando o banco e retornando uma lista ordenada por ID.
- Implementar `POST /tasks` inserindo título e status inicial no banco e retornando a tarefa criada com HTTP `201 Created`.
- Usar placeholders `?` e parâmetros separados para inserir valores, sem montar SQL por interpolação de strings.
- Converter o valor inteiro de `completed` do SQLite para `bool` nas respostas da API.

### 🛠️ Complete as operações por ID

#### Descrição
Implemente consulta, atualização e remoção de tarefas persistidas, mantendo os códigos HTTP e o formato de resposta da API anterior.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para consultar a tarefa no SQLite.
- Implementar `PATCH /tasks/{task_id}` para atualizar o campo `completed` no banco.
- Implementar `DELETE /tasks/{task_id}` para remover a tarefa.
- Retornar HTTP `404 Not Found` quando o ID não existir e HTTP `204 No Content` após uma remoção bem-sucedida.
- Confirmar a persistência criando uma tarefa, reiniciando o servidor e consultando a mesma tarefa novamente.
- Usar consultas parametrizadas também nas operações por ID.

Para executar a API, instale FastAPI e Uvicorn com `pip install fastapi uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`. Teste os endpoints pela documentação interativa em `http://127.0.0.1:8000/docs`.
