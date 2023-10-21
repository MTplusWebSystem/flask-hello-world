from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/gl/url=<path:url>', methods=['GET'])
def gl(url):
    full_url = f'http://{url}'
    try:
        response = requests.get(full_url)
        response_json = response.json()
        return jsonify(response_json), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cg4/url=<path:url>', methods=['GET','POST'])
def fourg(url):
    try:
        full_url = f'http://{url}'
        req_data = request.get_json()
        user = req_data.get("user")
            
        headers = {"Content-Type": "application/json"}
        data = {
            "user": user
        }
        json_data = json.dumps(data)
        response = requests.post(full_url, data=json_data, headers=headers)
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
