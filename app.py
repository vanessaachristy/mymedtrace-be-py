from flask import Flask, request
import spacy

app = Flask(__name__)

# Load spaCy model outside of the route functions
med7 = spacy.load("en_core_med7_lg")


@app.route("/")
def home():
    # text = 'Paracetamol of 100mg and Phenylephrine HCL 5mg of for the next 14 days.'
    # doc = med7(text)
    # return [(ent.text, ent.label_) for ent in doc.ents]
    return "hello flask"

@app.route("/parseMedication", methods=['POST'])
def parseMedication():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            text = request.json['text']
        doc = med7(text)
        return [(ent.text, ent.label_) for ent in doc.ents]



if __name__ == "__main__":
    app.run(port=6000, debug=True)