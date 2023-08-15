# API - É um lugar para disponibilizar recursos e/ou funcionalidades.
# 1. Objetivo - Criar uma api que disponibiliza a consulta, criação, edição de livros.
# 2. URL base - localhost.com
# 3. Endpoints -
# - localhost/livros (GET) - Obter todos os livros
# - localhost/livros (POST) - Adicionar livro
# - localhost/livros/id (GET) - Obter um livro específico (por id)
# - localhost/livro/id (PUT) - Modificar um livro (por id)
# - localhost/livro/id(DELETE) - Deletar um livro (por id)
# 4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Tomates Verdes Fritos',
        'autor': 'Fannie Flagg'
    },
    {
        'id': 2,
        'titulo': 'Hollywood',
        'autor': 'Charles B'
    },
    {
        'id': 3,
        'titulo': 'Frankenstein',
        'autor': 'Mary Shelley'
    }
]

# Consultar(todos)


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar


@app.route('/livros/', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
