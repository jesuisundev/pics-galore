from flask import Flask
import providers.giphy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Pics Galore'

@app.route('/giphy')
def giphy():
    dataFromGiphy = providers.giphy.getDataFromGiphy()
    return dataFromGiphy