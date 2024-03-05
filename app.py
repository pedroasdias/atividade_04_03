from flask import Flask, request

app = Flask(__name__)

livros = [
    {"titulo": "Assassinato no Expresso do Oriente", "infos":
        [
            {"autor": "Agatha Christie", "preco": 32.99, "genero": "Ficção Policial"}
        ]
    },
     {"titulo": "O Cemitério", "infos":
        [
            {"autor": "Stephen King", "preco": 12.35, "genero": "Horror"}
        ]
    }
    ]


#127.0.0.1:5000/livros
@app.get("/livros")
def get_livros():
    return {"livros": livros}

#127.0.0.1:5000/viagens/COLOQUEOautorAPESQUIAR
@app.get("/livros/<string:titulo>")
def get_livro_by_titulo(titulo):
    for livro in livros:
        if livro["titulo"] == titulo:
            return livro
    return {"message": "Viagens not found"}, 404

#127.0.0.1:5000/livros/autorAPESQUISAR/info
@app.get("/livros/<string:titulo>/infos/")
def get_infos_in_livros(titulo):
    for livro in livros:
        if livro["titulo"] == titulo:
            return {"infos": livro["infos"]}
    return {"message": "Livros not found"}, 404

#post 127.0.0.1:5000/livros
@app.post("/livros")
def create_livros():
    request_data = request.get_json() #pega o conteudo do body
    new_livros = {"titulo": request_data["titulo"], "infos": []}
    livros.append(new_livros) #insere o payload na viagens
    return new_livros, 201

#post 127.0.0.1:5000/livros/autorAINSERIR 
@app.post("/livros/<string:titulo>/infos")
def create_item(titulo):
    request_data = request.get_json()
    for livro in livros:
        if livro["titulo"] == titulo:
            new_info = {"autor": request_data["autor"], "preco": request_data["preco"], "genero": request_data["genero"]}
            livro["infos"].append(new_info)
            return new_info, 201
    return {"message": "Titulo nao encontrado "}, 404


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)