livros = [
    {"titulo": "Harry Potter e o Cálice de Fogo", "Autor": "J.K Rowling", "Ano de Lançamento": 2000, "Favorito":0 },
    {"titulo": "Diário de um banana - Dias de Cão", "Autor": "Jeff Kinney", "Ano de Lançamento": 2009, "Favorito":0 },
    {"titulo": "Maze Runner - Prova de Fogo", "Autor": "James Dashner", "Ano de Lançamento": 2010, "Favorito":0 },
    {"titulo": "O Pequeno Príncipe", "Autor": "Antoine de Sant-Exupéry", "Ano de Lançamento": 1943, "Favorito":0 },
]

for livro in livros:
    if livro["titulo"] == "Maze Runner - Prova de Fogo":
        livro["favorito"]=1

print(livros)