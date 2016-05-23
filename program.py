import requests
import bs4

response = requests.get('http://www.wwoofjapan.com/main/index.php?option=com_comprofiler&task=usersList&listid=11&Itemid=520&lang=en')
strBegin = html.find("cbUserURLs = new Array(") + 23
strEnd = html.find(");", strBegin)


"""
soup = bs4.BeautifulSoup(response.text)
soup
hostcodes = [span.get_text() for span in soup.select('span.cbUserListFC_cb_hostcode')]
hostcodes
"""