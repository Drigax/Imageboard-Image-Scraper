import re
import urlparse

__all__ = ['Links']

class Links (object):
    
    def __init__ (self):
        """
        Utility class for URL creation.
        """
        self.scheme = 'http'
        self.netloc = 'nota.real.netloc'
        self.apiloc = 'nota.real.apiloc'
        self.imgloc = 'nota.real.imgloc'

    board_pattern  = re.compile(r'/(\w+)$')
    page_pattern   = re.compile(r'/(\w+)/(\d+)$')
    thread_pattern = re.compile(r'/(\w+)/thread/(\d+)')

    def __makeURL (self, path, netloc, fragment=''):
        """
        Creates an URL based on path, whether it is an API URL and optionally
        a fragment for a specific post.
        """
        return urlparse.urlunparse (
            urlparse.ParseResult (
                scheme   = self.scheme,
                netloc   = netloc,
                path     = path,
                params   = '',
                query    = '',
                fragment = fragment
            )
        )

    def createURL (self, path, fragment=''):
        """
        Generates an URL based on a specific path and an optional fragment.
        """
        return self.__makeURL(path, self.netloc, fragment)

    def createAPIURL (self, path):
        """
        Generates an API URL based on a specific path.
        """
        return self.__makeURL(path, self.apiloc)

    def createImageURL (self, path):
        """
        Generates an Image URL based on a specific path.
        """
        return self.__makeURL(path, self.imgloc)

class FourChanLinks (Links):
    def __init__ (self):
        """
        Utility class for URL creation.
        """
        self.scheme = super(FourChanLinks,self).scheme
        self.netloc = 'boards.4chan.org'
        self.apiloc = 'a.4cdn.org'
        self.imgloc = 'i.4cdn.org'

class ArchivedMoeLinks (Links):
    def __init__ (self):
        """
        Utility class for URL creation.
        """
        self.scheme = super(ArchivedMoeLinks,self).scheme
        self.netloc = 'archived.moe'
        self.apiloc = 'archived.moe'
        self.imgloc = 'archived.moe'

class TheBArchiveLinks(Links):
    def __init__ (self):
        """
        Utility class for URL creation.
        """
        self.scheme = super(TheBArchiveLinks,self).scheme
        self.netloc = 'thebarchive.com'
        self.apiloc = 'thebarchive.com'
        self.imgloc = 'thebarchive.com'

