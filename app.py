from flask import Flask

app = Flask("__name__")

frutinhas = []

@app.get("/criarfrutas/nome=<nomeFruta>")
def criarfruta(nomeFruta):
    frutinhas.append(nomeFruta)
    return frutinhas

@app.get("/verfrutas")
def ListarFrutas():
    return frutinhas

@app.get("/verfruta/id=<idfruta>")
def PegarFruta(idfruta):
    try:
        idfruta = int(idfruta)
        return frutinhas[idfruta]
    except:
        return "Fruta não existe."
    
    #criar rota para contagem de fruta
    
app.run(port=6642)