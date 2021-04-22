from strenum import StrEnum


class Instance:
    """Create instance of video/sound"""

    def __init__(self, url, form, video_id, title):
        self._url = url
        self._format = Format.create(data=form)
        self._video_id = video_id
        self._title = title

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
    def options(self):
        """returns options for format"""
        return {'outtmpl': f"downloads/{self.title}.{self.format}"}


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
