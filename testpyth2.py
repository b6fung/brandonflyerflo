import urllib2
import sys
# gets the url from the user 
# this program takes in a url from the user that is a reddit url
# it then saves the alien image in the folder in which this program
# is stored
url = sys.argv[1]
page = urllib2.urlopen(url)
page = page.read()
index = page.find("header-img")
page = page[index:]
index = page.find("src")
index = index + 5
i = index
while page[i]!='\"':
    i=i+1
page = page[index:i]
print page
imgdata = urllib2.urlopen(page).read()
op = open('alien','wb')
op.write(imgdata)
op.close
