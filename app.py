from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello world"

@app.route("/about")
def about():
    return "Página sobre"

# habilita logs do servidor
if __name__ == "__main__":  ## regra para uso local - DESENVOLVIMENTO
    app.run(debug=True)