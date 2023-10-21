from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/api/glmod', methods=['GET'])
def intermediate():
    # Obtém a URL com censura do parâmetro da solicitação
    url = request.args.get('http')

    # Faz uma solicitação para a URL com censura
    response = requests.get(url)

    # Retorna a resposta do servidor com censura
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(debug=True)
