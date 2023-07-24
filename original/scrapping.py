import requests

# https://www.youtube.com/watch?v=PF8jrZVfmVM
url = input("링크 입력: ")
response = requests.get(url)

# filename = "url.txt"
# f = open(filename, mode = "w", encoding = "utf-8")
# f.write(response.text)
# f.close()

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "lxml")