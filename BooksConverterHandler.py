from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def homePage():
    # do your things here
    print("/")
    return "It works!"

@app.route("/speechToText")
def speechToText():
    print("/stt")
    # do your things here
    os.system('SpeechToText.py')
    return "It works!"

@app.route("/eyeTracking", methods = ['GET'])
def eyeTracking():
    print("/ET")
    # do your things here
    os.system('EyeTracking2.py')
    return "It works!"

@app.route("/pdfToDoc", methods = ['POST', 'GET'])
def BooksConverter():
    print("/PDF TO DOC")
    if request.method == 'POST':
        result = request.form
        result = result.get('browse')
        print(result)

    BooksConverter.PdfToDoc(result)
    print("it works")
    return "it works"


if __name__ == "__main__":
    app.run()