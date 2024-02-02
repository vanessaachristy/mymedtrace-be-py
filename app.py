from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import spacy

app = Flask(__name__)

CORS(app, origins="http://localhost:3001", supports_credentials=True, methods=['GET', 'HEAD', 'PUT', 'PATCH', 'POST', 'DELETE'])

# Load spaCy model outside of the route functions
med7 = spacy.load("en_core_med7_lg")

@app.route("/parseMedication", methods=['POST', 'OPTIONS'])
def parseMedication():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS preflight successful'})
        response.headers.add("Access-Control-Allow-Methods", "POST")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Credentials", "true")
        return response

    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            text = request.json['text']
            doc = med7(text)

            parsedList = []
            seen = set()
            current_dict = {}
            for ent in doc.ents:
                if ent.label_ in seen:
                    parsedList.append(current_dict)
                    current_dict = {}
                    seen = set()
                
                current_dict[ent.text] = ent.label_
                seen.add(ent.label_)
            
            if len(current_dict) != 0:
                parsedList.append(current_dict)

            response = make_response(jsonify(parsedList))
            return response

if __name__ == "__main__":
    app.run(port=3002, debug=True)
