#import
from flask import Flask

#Création instance Flask
app = Flask(__name__)

#Création route vers la page HTML
@app.route('/')
def home():
    return '<h1>On adore le DevOps </h1>'

#Lancement appli F
if __name__ == '__main__':
    app.run(host='0.0.0.0')
