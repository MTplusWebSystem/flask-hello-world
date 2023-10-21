from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/glmod/http=<path:url>', methods=['GET'])
def intermediate(url):
    # Monta a URL completa com base no parâmetro passado
    full_url = f'http://{url}'

    # Faz uma solicitação para a URL com censura
    response = requests.get(full_url)

    # Retorna a resposta do servidor com censura
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(debug=True)
