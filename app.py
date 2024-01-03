from flask import Flask, jsonify, request

app = Flask(__name__)
filmes = [
    {
        'id': 1,
        'titulo': 'Kill Bill vol. 1',
        'diretor': 'Quentin Tarantino',
        'ano': 2003,
        'genero': ['Ação', 'Crime', 'Thriller'],
        'atores_principais': ['Uma Thurman', 'Lucy Liu', 'Vivica A. Fox'],
        'classificacao': '+18',
        'sinopse': 'A Noiva, uma ex-assassina, acorda de um coma e parte em uma jornada de vingança contra seus antigos colegas de equipe que a traíram no dia de seu casamento.',
    },
    {
        'id': 2,
        'titulo': 'Kill Bill vol. 2',
        'diretor': 'Quentin Tarantino',
        'ano': 2004,
        'genero': ['Ação', 'Crime', 'Thriller'],
        'atores_principais': ['Uma Thurman', 'David Carradine', 'Michael Madsen'],
        'classificacao': '+18',
        'sinopse': 'A Noiva continua sua busca por vingança contra os membros restantes de sua antiga equipe, culminando em um confronto final com seu antigo mentor e líder.',
    },
    {
        'id': 3,
        'titulo': 'Suspiria',
        'diretor': 'Dario Argento',
        'ano': 1977,
        'genero': ['Horror', 'Mistério', 'Thriller'],
        'atores_principais': ['Jessica Harper', 'Stefania Casini', 'Flavio Bucci'],
        'classificacao': '+18',
        'sinopse': 'Uma jovem bailarina vai para uma prestigiada escola de dança na Europa, mas descobre que a escola abriga segredos sinistros e práticas ocultas.',
    },
]

#Consultar todos os filmes
@app.route('/filmes', methods=['GET'])
def obter_filmes():
    return jsonify(filmes)


@app.route('/filmes/<int:filme_id>', methods=['GET'])
def get_filme(filme_id):
    for filme in filmes:
        if filme['id'] == filme_id:
            return jsonify(filme)
    
    return jsonify({'mensagem': 'Filme não encontrado'}), 404



@app.route('/filmes', methods=['POST'])
def add_filme():
    novo_filme = request.get_json()
    filmes.append(novo_filme)
    return jsonify({'mensagem': 'Filme adicionado com sucesso', 'id': novo_filme['id']}), 201  # Código 201 indica criação


@app.route('/filmes/<int:filme_id>', methods=['PUT'])
def update_filme(filme_id):
    for filme in filmes:
        if filme['id'] == filme_id:
            dados_atualizados = request.get_json()
            filme.update(dados_atualizados)
            return jsonify({'mensagem': 'Filme atualizado com sucesso'})
    return jsonify({'mensagem': 'Filme não encontrado'}), 404

@app.route('/filmes/<int:filme_id>', methods=['DELETE'])
def delete_filme(filme_id):
    global filmes
    filmes = [f for f in filmes if f['id'] != filme_id]
    return jsonify({'mensagem': 'Filme excluído com sucesso'}), 200




app.run(port=5000, host='localhost', debug=True)

