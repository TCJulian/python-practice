"""
Exercise from:
http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

Objective:
Using the requests and BeautifulSoup Python libraries, print to the screen the
full text of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print
out the text to the screen so that you can read the full article without having
to click any buttons.

This will just print the full text of the article to the screen. It will not
make it easy to read, so next exercise we will learn how to write this text
to a .txt file.
"""
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
text = soup.find_all("p")
for i in text:
    content = i.string
    if content:
        print(content)
