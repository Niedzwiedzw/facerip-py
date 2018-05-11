from flask import Flask
from flask import request
from text_to_speech.text_to_speech import AudioFile
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
    if __name__ == '__main__':
        text = input('co chcesz przeczytac? \n >> ')
        with AudioFile(text) as f:
            f.play()
