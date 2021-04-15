from strenum import StrEnum


class Instance:
    """Create instance of video/sound"""

    def __init__(self, url, form):
        self.url = url
        self.format = Format.create(data=form)

    @property
    def get_url(self):
        """returns url"""
        return self.url

    @property
    def get_format(self):
        """returns format"""
        return self.format

    @property
    def options(self):
        """returns options for format"""
        if self.format == Format.MP3:
            return {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        return {}


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
