from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench/<textToTranslate>")
def englishToFrench(textToTranslate):
    translation = translator.english_to_french(textToTranslate)
    return translation

@app.route("/frenchToEnglish/<textToTranslate>")
def frenchToEnglish(textToTranslate):
    translation = translator.french_to_english(textToTranslate)
    return translation

@app.route("/")
def renderIndexPage():
    render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
