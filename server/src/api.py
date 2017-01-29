from flask import Flask, request, Response
from flask_cors import CORS
from rdf import search_phones
import json

app = Flask(__name__)
CORS(app)


@app.route('/api/search/', methods=['POST'])
def search():
    request_params = request.get_json()
    search_result = search_phones(request_params)
    response_data = [str(x[0]) for x in search_result]
    return Response(json.dumps(response_data),  mimetype='application/json')


if __name__ == '__main__':
    app.run()
