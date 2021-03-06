from . import WebEntity
from . import Board

__all__ = ['Site']

class Site (WebEntity):
    """
    Represents the site in its entirety.
    """
    default_object = {'boards':[]}

    def __init__ (self, links):
        """
        Initializes the site, provided a SiteLinks object that will allow this site to generate URLs.
        """
        self.links = links
        pass

    def __repr__ (self):
        """
        Returns a string representation fit for eval.
        """
        return '{self.__class__.__name__}()'.format(self=self)

    @property
    def apiurl (self):
        """
        Returns an url to the corresponding API json page.
        """
        return self.links.createAPIURL (
            '/boards.json'
        )

    @property
    def url (self):
        """
        Returns an url to the site.
        """
        return self.links.createURL('/')

    def process (self):
        """
        Returns the Board instances you get by evaluating the site.
        """
        return map (
            lambda board : Board (
                str(board['board']), self
            ),
            self.download_and_decode()['boards']
        )
