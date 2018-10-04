from .torrentSearcher import TorrentSearcher
from .torrent import Torrent
import re

class ExtratorrentSearcher(TorrentSearcher):

    """docstring for ExtratorrentSearcher."""
    def __init__(self, torrentName):
        print("ExtratorrentSearcher: __init__")
        super(ExtratorrentSearcher, self).__init__(torrentName)
        self.html = "extratorrent.ag"


    def searchForTorrents(self):
        print("ExtratorrentSearcher: searchForTorrents")
        if self._checkAvailability() == False:
            self.htmlResponse = '<div class="alert alert-danger" role="alert"> <a href="#" class="alert-link">Error: extratorrent is unavailable!</a> </div>';
            return
        self.__prepareRequestAddress()
        self._obtainTorrentsRawHtml()
        self.__parseTorrentsRawHtml()

    def __prepareRequestAddress(self):
        print("ExtratorrentSearcher: __prepareRequestAddress")
        parsedTitle = self.torrentName.replace(" ", '%20')
        # self.requestAddress = "{}/search/?search={}&s_cat=&pp=&srt=seeds&order=desc".format(self.html, parsedTitle)
        self.requestAddress = "/search/?search={}&s_cat=&pp=&srt=seeds&order=desc".format(parsedTitle)

    def __parseTorrentsRawHtml(self):
        p = re.compile('<tr class="tlr">.+?<\/tr>')
        m = p.findall(self.torrentsRawHtml)
        print(m[0])
        self.__extractTitle(m[0])
        newTorrent = Torrent(title = self.__extractTitle(m[0]))

    def __extractTitle(self, singleTorrentRawHtml):
        title = "dupa"
        p = re.compile('(?=dn=).+?(?=&)')
        m = p.findall(singleTorrentRawHtml)
        m[0] = m[0].replace("dn=", "")
        print(m[0])
        return m[0]


    def getHtmlResponse(self):
        print("ExtratorrentSearcher: getHtmlResponse")
        return self.htmlResponse
