from bs4 import BeautifulSoup
import urllib.request
from typing import List

desireTag: List[str] = ["수필", "소설", "장편소설", "중편소설", "단편소설", "동화"]
URL: str = "ko.wikisource.org/w/index.php?title=특수:모든문서"

def form(title: str, writer: str, contents: str) -> str:
    pass


def crawl(title: str) -> str:
    fp = urllib.request.urlopen("ko.wikisource.org/wiki/" + title.replace(" ", "_"))
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    soup = BeautifulSoup(mystr)
    writer: str = soup.select(".fn")[0].get_text()
    contents: str = "\n".join( (s.get_text() for s in soup.select(".mw-parser-output")) )
    return form(title, writer, contents)


def main():
    i: int = 0
    next: str = '"조선어 신 철자법" 일부 개정에 대하여'
    while True:
        fp = urllib.request.urlopen(URL + "&" + next.replace(" ", "+"))
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        soup = BeautifulSoup(mystr)


if __name__ == "__main__":
    main()
