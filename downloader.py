from __future__ import unicode_literals
from inception import Instance, Format
import eel
import youtube_dl

eel.init('web')


@eel.expose
def download(data):
    instance = Instance(data['url'], data['format'])
    with youtube_dl.YoutubeDL(instance.options) as ydl:
        ydl.download([instance.get_url])


eel.start('index.html', size=(750, 600))
