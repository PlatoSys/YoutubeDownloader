"""Downloading Module"""
from __future__ import unicode_literals
from python_modules.inception import Instance
import eel
import youtube_dl

eel.init('web')


@eel.expose
def download(data):
    with youtube_dl.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(data['url'], download=False)
        instance = Instance(data['url'], data['format'], info_dict.get('id', None),
                            info_dict.get('title', None))

    with youtube_dl.YoutubeDL(instance.options) as ydl:
        ydl.download([instance.url])


eel.start('index.html', size=(750, 600))
