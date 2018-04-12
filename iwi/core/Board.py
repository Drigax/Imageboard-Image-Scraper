from ..web import Links

from . import WebEntity
from . import Thread

__all__ = ['Board']

class Board (WebEntity):
    """
    Represents a board.
    """
    default_object = []
    
    def __init__ (self, board, site):
        """
        Initializes an instance from a board and a Site.
        """
        self.board = board
        self.site = site

    def __repr__ (self):
        """
        Returns a string representation fit for eval.
        """
        return '{self.__class__.__name__}({self.board!r})'.format(self=self)

    @property
    def apiurl (self):
        """
        Returns an url to the corresponding API json page.
        """
        return self.site.links.createAPIURL (
            '/{self.board}/threads.json'.format(self=self)
        )

    @property
    def url (self):
        """
        Returns an url to the board.
        """
        return self.site.links.createURL('/{self.board}/'.format(self=self))

    def process (self):
        """
        Returns the Thread instances you get by evaluating the board.
        """
        pages   = self.download_and_decode()
        threads = []

        for page in pages:
            for thread in page['threads']:
                threads.append (
                    Thread(self.board, thread['no'], self.site)
                )

        return threads
