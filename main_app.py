from flask import Flask
from flask import request
from text_to_speech.text_to_speech import AudioFile
app = Flask(__name__)


@app.route('/read', methods=['get'])
def read_something():
    text = request.args.get('text', default='', type=str)
    with AudioFile(text) as f:
        f.play()
    return "czytam: `{}`".format(text) if text else 'uzycie: `/read?text=blablabla'


if __name__ == '__main__':
    if __name__ == '__main__':
        app.run(host='0.0.0.0')

