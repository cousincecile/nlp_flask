from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__, template_folder='template')


def byte_to_json(content):
    my_json1 = json.loads(content, strict = False)
    return my_json1



@app.route('/', methods =["GET", "POST"]) 
def index():
    if request.method == "POST": 
        question = request.form.get("question") 
        url = "http://localhost:5000/debate/" + str(question)
        response = requests.get(url)
        return render_template('response.html', content_gauche = byte_to_json(response.text)["gauche"], content_droite = byte_to_json(response.text)["droite"])
    return render_template('index.html')
app.run()



