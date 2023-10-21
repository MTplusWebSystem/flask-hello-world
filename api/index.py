from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/glmod/http=<path:url>', methods=['GET'])
def intermediate(url):
    full_url = f'http://{url}'
    try:
        response = requests.get(full_url)
        response_json = response.json()
        return jsonify(response_json), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
