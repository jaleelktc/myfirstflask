import bs4 as bs
import urllib
#import requests
import urllib3.request
source = urllib.urlopen('https://www.amazon.com/Fire-Tablet-Alexa-Display-Blue/product-reviews/B018Y227MY/ref=cm_cr_getr_d_show_all?pageNumber=1&reviewerType=all_reviews')
s = source.read()
soup=bs.BeautifulSoup(s,'lxml')
#print (soup.find_all("a"))
#for ida in soup.find_all("div"):
 #   print ida

#soup = bs.BeautifulSoup(s)

rev=soup.findAll("div",{'class':'a-section a-spacing-none review-views celwidget'})
for review in rev:
    print (review["id"])

