from flask import Flask, render_template, request
import requests
import json


BASE_URL = "http://127.0.0.1:5000/debate/"

if __name__ == "__main__":


    app = Flask(__name__, template_folder="template")

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route("/answer", methods = ["POST", "GET"])
    def response():

        question = request.form.get("question")
        answer = requests.get(BASE_URL + str(question)).text
        dictAnswer = json.loads(answer, strict=False)

        return render_template("response.html", content_gauche=dictAnswer["gauche"], content_droite=dictAnswer["droite"])



    app.run(port=8000, debug=True)

