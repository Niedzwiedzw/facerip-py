from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/read', methods=['POST'])
def read_something():
    return str(f"""you are reading this in IVONA voice:
{ request.data }
"""
)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
