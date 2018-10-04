import http.client
from .torrent import Torrent

class TorrentSearcher():
    """docstring for TorrentSearcher."""

    def __init__(self, torrentName):
        print("TorrentSearcher: __init__")
        self.html = ""
        self.htmlResponse = ""
        self.torrentName = torrentName
        self.torrentsList = []

        #conn.request("GET", "/")
        #r1 = conn.getresponse()
        #print(r1.status, r1.reason)
        #data1 = r1.read()  # This will return entire content.
        # print(str(data1)) 

    def _prepareConnection(self):
        print("TorrentSearcher: _prepareConnection")
        self.conn = http.client.HTTPSConnection(self.html)

    def _checkAvailability(self):
        print("TorrentSearcher: _checkAvailability")
        self._prepareConnection()
        self.conn.request("GET", "/")
        r1 = self.conn.getresponse()
        # print(r1.status, r1.reason)
        if r1.status != 200:
            return False
        return True

    def _obtainTorrentsRawHtml(self):
        print("TorrentSearcher: _obtainTorrentsRawHtml")
        self.conn = http.client.HTTPSConnection(self.html)
        self.conn.request("GET", self.requestAddress)
        r1 = self.conn.getresponse()
        # print(r1.status, r1.reason)
        # TODO: add check for status
        self.torrentsRawHtml = str(r1.read())  # This will return entire content.
        # print(str(self.torrentsRawHtml))


    def getHtmlResponse(self):
        print("TorrentSearcher: getHtmlResponse")
        self.html = '<p>It works!</p>' + "\n"
        self.html += '<p>' + self.torrentName + '</p>' + "\n"
        return self.html
