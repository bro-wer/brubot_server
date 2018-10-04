class TorrentSearcher(object):
    """docstring for TorrentSearcher."""

    def __init__(self, torrentName):
        self.torrentName = torrentName
        self.html = ""

    def getHtmlResponse(self):
        self.html = '<p>It works!</p>' + "\n"
        self.html += '<p>' + self.torrentName + '</p>' + "\n"
        return self.html
