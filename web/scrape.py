import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://www.genius.com/Young-thug-hercules-lyrics'

def scrape(url):
    # add headers since genius.com blocks beautiful soup with no headers
    header = {'User-Agent':'Mozilla/5.0'}
    req = urllib2.Request(url=url, headers = header)
    html = urllib2.urlopen(req)
    soup = BeautifulSoup(html)
    # see if scrape works
    # print (soup.prettify())

    lyrics = ''
    # lyrics are all in <a> tags with class = 'referent'
    # note that this only works with lyrics that are annotated.
    for row in soup('a',{'class':'referent'}):
        text = ''.join((row.findAll(text = True)))
        data = text.strip() + '.' '\n'
        lyrics += data

    return lyrics