from flask import Flask, render_template, jsonify, request
import functions

app = Flask(__name__)

@app.route('/')
def index():
    data = functions.get_humedad()
    print(data)
    return render_template('app.html', data=data)

@app.route('/post', methods=["POST"])
def insert_value():
    data = request.get_json()
    humedad = data['humedad']
    result = functions.insert_humedad(humedad)
    return jsonify(result)

app.run(host='0.0.0.0', port=8000, debug=False)