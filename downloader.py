from __future__ import unicode_literals
import io
import pyqrcode
from base64 import b64encode
import eel
import youtube_dl

eel.init('web')


@eel.expose
def download(data):
    link = data
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


eel.start('index.html', size=(250, 250))
