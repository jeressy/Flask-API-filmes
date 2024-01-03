# Movie API (Flask)

Este é um exemplo simples de API para entender os métodos GET, PUT, POST e DELETE. Não é recomendado para uso em produção e não inclui autenticação ou validação extensiva. É apenas uma implementação básica para fins educacionais.

## Rotas disponíveis

### Consultar todos os filmes

Endpoint:
```
GET /filmes
```
Retorna uma lista de todos os filmes cadastrados.

### Consultar um filme específico

Endpoint:
```
GET /filmes/<int:filme_id>
```
Retorna os detalhes de um filme com o ID especificado. Se o filme não for encontrado, retorna um erro 404.

### Adicionar um novo filme

Endpoint:
```
POST /filmes
```
Permite adicionar um novo filme. Os detalhes do filme devem ser enviados no corpo da solicitação em formato JSON. Retorna uma mensagem de sucesso junto com o ID atribuído ao novo filme.

### Atualizar informações de um filme

Endpoint:
```
PUT /filmes/<int:filme_id>
```
Permite atualizar as informações de um filme existente. Os detalhes atualizados do filme devem ser enviados no corpo da solicitação em formato JSON. Retorna uma mensagem de sucesso se o filme for encontrado e atualizado, caso contrário, retorna um erro 404.

### Excluir um filme

Endpoint:
```
DELETE /filmes/<int:filme_id>
```
Permite excluir um filme com o ID especificado. Retorna uma mensagem de sucesso se o filme for encontrado e excluído, caso contrário, retorna um erro 404.

## Uso da API

1. Execute o aplicativo Flask executando o script `app.py`.
   ```
   python app.py
   ```




