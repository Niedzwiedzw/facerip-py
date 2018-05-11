import uuid
import os
import requests
from settings import AUDIO_FILES_DIR

DOWNLOAD_BASE_URL = 'http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={text}&tl={language}'

LANGUAGES = ['pl', 'en']


class AudioFile:
    def __init__(self, text: str):
        self.text = text
        self._file_id = str(uuid.uuid4())
        self._filepath_mp3 = os.path.join(AUDIO_FILES_DIR, self._file_id + '.mp3')
        self._filepath_wav = os.path.join(AUDIO_FILES_DIR, self._file_id + '.wav')

    def _download_audio(self):
        audio_bytes = requests.get(DOWNLOAD_BASE_URL.format(**{
            'text': 'Witaj swiecie',
            'language': 'pl'
        })).iter_content()

        with open(self._filepath_mp3, 'ab') as f:
            for chunk in audio_bytes:
                f.write(chunk)

    def _convert_audio(self):
        os.system('ffmpeg -i {} {}'.format(self._filepath_mp3, self._filepath_wav))

    def play(self):
        os.system('agplay {}'.format(self._filepath_wav))

    def __enter__(self):
        self._download_audio()
        self._convert_audio()
        return self

    def __exit__(self, *args):
        os.remove(self._filepath_wav)
        os.remove(self._filepath_mp3)


def read(text: str):
    print("I am reading: {}".format(text))


if __name__ == '__main__':
    text = input('co chcesz przeczytac? \n >> ')
    with AudioFile(text) as f:
        f.play()
