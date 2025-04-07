# ✨ Desenvolvimento de uma API RESTful para Posts

## 1. 📚 Introdução
Neste documento, será descrito o desenvolvimento de uma API RESTful para gerenciar posts. A API permitirá a criação, leitura, atualização e exclusão de posts, seguindo as boas práticas do padrão REST.

## 2. 🛠 Descrição
A API será responsável por gerenciar posts, permitindo que os usuários possam criar novos conteúdos, visualizar publicações existentes, editar posts já criados e removê-los quando necessário. A comunicação será feita por meio do protocolo HTTP, utilizando o formato JSON para troca de dados.

## 3. 💻 Tecnologias Utilizadas
A implementação da API será feita utilizando as seguintes tecnologias:
- **📝 Linguagem**: Python
- **🛠 Framework**: Flask

## 4. 🛠 Estrutura do Projeto
A organização do projeto seguirá a estrutura recomendada para desenvolvimento com Flask:
```
📁 api-posts/
├── 📁 controller/
│   │   ├── 📄 post_controller.py
│   📁 database/
│   │   ├── 📄 .env
│   │   ├── 📄 conexao.py
├── 📁 models/
│   │   ├── 📄 post.py
├── 📄 main.py
├── 📄 req.txt
```

## 5. 🛡️ Endpoints da API
A tabela abaixo apresenta os endpoints a serem desenvolvidos:

| ✉️ Método HTTP | 🔗 Endpoint        | 💃 Descrição                                    |
|------------|----------------|----------------------------------------------|
| GET        | /posts         | Retorna todos os posts                      |
| GET        | /posts/{id}    | Retorna um post específico                  |
| POST       | /posts         | Cria um novo post                           |
| PUT        | /posts/{id}    | Atualiza um post existente                  |
| DELETE     | /posts/{id}    | Remove um post                              |

## 6. 📚 Boas Práticas
Algumas boas práticas recomendadas para a API:
- ✨ Seguir os princípios RESTful para organização dos endpoints.
- ✅ Utilizar códigos de status HTTP adequados nas respostas.
- ⚠️ Implementar tratamento de erros para respostas mais claras e informativas.
- 🛠 Utilizar um sistema de versionamento para facilitar futuras atualizações.

## 7. 🔍 Considerações Finais
Esta API RESTful para posts servirá como um excelente exemplo prático para a aplicação dos conceitos de desenvolvimento web, utilizando Python e Flask. A implementação correta seguindo as boas práticas garantirá um sistema eficiente, seguro e de fácil manutenção.

## 8. 📚 Desafio: Representação dos Comentários
Para permitir interações nos posts, será implementado um sistema de comentários. Cada post poderá conter múltiplos comentários, possibilitando respostas e discussões. Abaixo está a estrutura dos endpoints relacionados aos comentários:

| ✉️ Método HTTP | 🔗 Endpoint                 | 💃 Descrição                          |
|------------|-------------------------|----------------------------------|
| GET        | /posts/{id}/comments    | Retorna todos os comentários do post |
| POST       | /posts/{id}/comments    | Adiciona um novo comentário ao post |
| DELETE     | /comments/{id}          | Remove um comentário pelo ID        |

A estrutura do modelo para os comentários será:
```json
{
  "id": 1,
  "post_id": 1,
  "autor": "Usuário X",
  "conteudo": "Este é um comentário.",
  "data_criacao": "2025-03-25T12:00:00Z"
}
```