
from flask import Flask, jsonify, request


app = Flask(__name__)

livros = [
    {
        'id' : 1,
        'titulo' : 'livro1',
        'autor' : 'autor1'
    },
        {
        'id': 2,
        'titulo' : 'livro2',
        'autor' : 'autor2'
    },
        {
        'id': 3,
        'titulo' : 'livro3',
        'autor' : 'autor3'
    },
        {
        'id': 4,
        'titulo': 'livro4',
        'autor' : 'autor4'
    },

]


error = [
    {
    'Error': 'file not find'
    }
]

#consultar(todos)
@app.route('/livros/',methods=['GET'])
def obter_livros():
    return jsonify(livros)


@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify(error)


#editar
@app.route('/livros/<int:id>',methods=['DELETE'])
def Deletar_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify(error)



@app.route('/livros/<int:id>',methods=['PUT'])
def update_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros)
    return jsonify(error)

app.run(port=5000,host='localhost',debug=True)