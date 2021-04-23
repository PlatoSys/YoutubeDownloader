"""Inception module which contains Types and Classes"""
from strenum import StrEnum
import os
import eel


class Instance:
    """Create instance of video/sound"""

    def __init__(self, url, form, video_id, title):
        self._url = url
        self._format = Format.create(data=form)
        self._video_id = video_id
        self._title = title
        self._progress = 0

    @property
    def url(self):
        """returns url"""
        return self._url

    @property
    def format(self):
        """returns format"""
        return self._format

    @property
    def video_id(self):
        """Returns video id"""
        return self._video_id

    @property
    def title(self):
        """returns video title"""
        return self._title

    @property
    def progress(self):
        """returns progress"""
        return self._progress

    def progress_update(self, value):
        self._progress = value

    @property
    def options(self):
        """returns options for format"""
        return {
            'outtmpl': f"downloads/{self.title}.{self.format}",
            'progress_hooks': [self.my_hook],
        }

    @eel.expose
    def my_hook(self, progress):
        eel.update_progress(self.progress)
        if progress['status'] == 'finished':
            file_tuple = os.path.split(os.path.abspath(progress['filename']))
            self.progress_update(100)
        if progress['status'] == 'downloading':
            percent = progress['_percent_str']
            percent = percent.replace('%', '')
            self.progress_update(float(percent))


class Format(StrEnum):
    MP3 = "MP3"
    MP4 = "MP4"

    @classmethod
    def create(cls, data):
        data = data.upper()
        if data == "MP3":
            return cls.MP3
        if data == "MP4":
            return cls.MP4
