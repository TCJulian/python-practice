# -------------------------------------------------------------------
#
# Exercise from: http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
#
# Objective:
# 1. Use the BeautifulSoup and requests Python packages to print out a list of
# all the article titles on the New York Times homepage.
#
# -------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.nytimes.com/")
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
titles = soup.find_all("h3")
for i in titles:
    print(i.string)
