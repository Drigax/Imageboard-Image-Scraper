import urlparse

from ..web import Links, FourChanLinks, ArchivedMoeLinks, TheBArchiveLinks

from . import WebEntity, Board, Page, Thread

__all__ = ['classify']

def classify (url):
    """
    Classifies an URL and returns the corresponding WebEntity derivative.
    """
    original = url

    if isinstance (url, WebEntity):
        return url

    if not isinstance (url, str):
        raise TypeError ('%s not valid type of imageboard URL' % type(url))

    if url.startswith('/'):
        url = url.lstrip('/')

    if url.endswith('/'):
        url = url.rstrip('/')

    siteLink = Links()
    if '4chan.org' in url:
        siteLink = FourChanLinks()
        
    elif 'archived.moe' in url:
        siteLink = ArchivedMoeLinks()
    elif 'thebarchive.com' in url:
        siteLink = TheBArchiveLinks()
    else:
        # if neither site was provied in the url, default to using 4chan links.
        # Though we should probably remove this, it doesnt make much sense.
        siteLink = FourChanLinks()
        url = '{}://{}/{}'.format(siteLink.scheme, siteLink.netloc, url)

    if not (
        url.startswith ('http://') or
        url.startswith ('https://')
    ):
        url = '{}://{}'.format(siteLink.scheme, url)

    path  = urlparse.urlparse(url).path

    match = siteLink.thread_pattern.match(path)
    if match:
        return Thread(*match.groups(), site = siteLink)

    match = siteLink.page_pattern.match(path)
    if match:
        return Page(*match.groups(), site = siteLink)

    match = siteLink.board_pattern.match(path)
    if match:
        return Board(*match.groups(), site = siteLink)

    raise ValueError ('invalid URL: %s' % repr(original))
