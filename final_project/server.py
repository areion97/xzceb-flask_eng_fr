from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation from Translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    a = Translator.english_to_french(textToTranslate)
    return a

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    a = Translator.french_to_english(textToTranslate)

    return a

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
