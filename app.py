from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/image', methods=['POST'])
def inspire():
    return jsonify('I am inspired')