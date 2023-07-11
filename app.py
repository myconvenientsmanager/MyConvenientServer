from flask import Flask
from flask_sslify import SSLify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, triple D!'

if __name__ == '__main__':
    app.run()
    sslify = SSLify(app)