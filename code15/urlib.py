import urllib2
response=urllib2.urlopen('http://www.cbnweek.com/v/article?id=5655&m=5d33ac8d9fc7325471fbce66227dbacb')
html=response.read()
print html