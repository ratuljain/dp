from math import floor
from urlparse import urlparse
import sqlite3
import string
import datetime
import urllib2
import webbrowser
import urllib2
import httplib
from BeautifulSoup import BeautifulSoup
counter = 4


# Converts the string into base62
def toBase62(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.lowercase + string.uppercase
    r = num % b
    res = base[r];
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

# Converts back to base 10
def toBase10(num, b = 62):
    base = string.digits + string.lowercase + string.uppercase
    limit = len(num)
    res = 0
    for i in xrange(limit):
        res = b * res + base.find(num[i])
    return res

def ifWebsiteExists(url):
    try:
        urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print(e.code)
    except urllib2.URLError, e:
        print(e.args)

def getTitle(url):
    try:
        soup = BeautifulSoup(urllib2.urlopen(url))
        return soup.title.string
    except:
        return None

# Processes the URL so that amazon.com and http://amazon.com are the same
# and only a single entry is made for both of them

def processURL(url):

    if urlparse(url).scheme == '':
            url = 'http://' + url
    return url

# Inserts the url and it's resulting shortened URL into the table
def insertURL(url):
    url = processURL(url)
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    x = c.execute("SELECT count(*) from urls;")
    sort_str = x.fetchall()[0][0]
    sort = int(sort_str) + 1
    now = datetime.datetime.now()
    short = "http://short.nr/"+toBase62(sort)
    title = getTitle(url)
    try:
        c.execute('insert into urls (url, short, hits, t, title) values (?, ?, ?, ?, ?) ', [url, short, 0, now, title])
    except:
        pass
    conn.commit()
    conn.close()

# Inserts URL into the database and returns the resulting shortened version
# Uses the insertURL() method from above. http://short.nr/ is the domain of shortening website.

def shortURL(url):
    url = processURL(url)
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT id FROM urls WHERE url = ?", (processURL(url),))
    data=c.fetchall()
    if not data:
        insertURL(url)
    c.execute("SELECT id FROM urls WHERE url = ?", (processURL(url),))
    data=c.fetchall()[0][0]
    conn.close()
    return "http://short.nr/" + str(data)

# Converts the shortened URL back to the orignal one and
# redirects to the orignal URL

def redirect(url):
    id = toBase10((urlparse(url).path[1:]))
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT url FROM urls WHERE id = ?", (id,))
    orignalUrl = c.fetchall()[0][0]
    # return orignalUrl# +  "  --->   " + url    # Uncomment for to print the mapping
    webbrowser.open(orignalUrl)
    conn.close()

def hits(url):
    url = processURL(url)
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT hits FROM urls WHERE url = ?", (url,))
    print "Hits for " + url + " is " + str(c.fetchall()[0][0])

# def search

# inserts URL, shortens it then converts it back to the
# orignal URL and redirects to it and increments the hits counter.

def doStuff(url):
    a = shortURL(url)
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("UPDATE urls SET hits=(hits+1) WHERE url = ?", ((processURL(url),)))
    conn.commit()
    print "Here's your shortened URL  " + a
    print ""
    print "Do you want to visit the shortened url? (y/n)"
    if(raw_input() == 'y'):
        redirect(a)
    conn.close()


conn = sqlite3.connect('example.db')
c = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS urls (
        id integer primary key autoincrement,
        url string not null unique,
        short string,
        hits int,
        t TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,
        title string
        ); '''

c.execute(sql)


#####################################  test

# doStuff("https://www.python.org")
print ifWebsiteExists("http://lolsnadhbaf.com")
# hits("http://apple.com")
# c.execute('''SELECT * FROM urls''')
# print c.fetchall()

c.close()