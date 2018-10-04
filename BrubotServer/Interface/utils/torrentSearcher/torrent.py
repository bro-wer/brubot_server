class Torrent(object):
    """docstring for Torrent."""
    def __init__(self, title):
        self.title = title
        self.printme()

    def printme(self):
        print("\nNEW TORRENT")
        print("\ttitle: " + str(self.title))
