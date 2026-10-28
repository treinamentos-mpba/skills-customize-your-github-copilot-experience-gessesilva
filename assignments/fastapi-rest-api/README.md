# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI. Você praticará métodos HTTP, modelos de dados com Pydantic, códigos de status e tratamento de recursos inexistentes.

## 📝 Tarefas

### 🛠️ Configure a API e liste tarefas

#### Descrição
Complete o código inicial para criar a aplicação FastAPI e implementar endpoints de verificação e listagem. Instale as dependências com `pip install fastapi uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`; a documentação interativa ficará disponível em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI chamada `app` no arquivo `starter-code.py`.
- Implementar `GET /health`, retornando `{"status": "ok"}`.
- Implementar `GET /tasks`, retornando a lista de tarefas, inicialmente vazia.

### 🛠️ Crie tarefas com validação

#### Descrição
Defina os modelos Pydantic necessários e implemente a criação de tarefas. Cada tarefa deve receber um identificador único e começar com o status incompleto.

#### Requisitos
O programa concluído deve:

- Usar `TaskCreate` para validar o título enviado no corpo da requisição.
- Representar cada tarefa com `id`, `title` e `completed`.
- Implementar `POST /tasks`, atribuindo um novo ID e definindo `completed` como `false`.
- Retornar a tarefa criada com o código HTTP `201 Created`.
- Permitir testar a criação pela documentação em `/docs`, enviando, por exemplo, `{"title": "Estudar FastAPI"}`.

### 🛠️ Consulte, atualize e remova tarefas

#### Descrição
Implemente operações para buscar uma tarefa pelo ID, atualizar seu status de conclusão e removê-la da lista.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para retornar a tarefa solicitada.
- Implementar `PATCH /tasks/{task_id}` para atualizar o campo `completed` usando um modelo Pydantic.
- Implementar `DELETE /tasks/{task_id}` e responder com o código HTTP `204 No Content` quando a tarefa for removida.
- Retornar `404 Not Found` nas operações por ID quando a tarefa não existir.
