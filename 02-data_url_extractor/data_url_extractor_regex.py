import re
import sys


def data_url_extractor(html_source):
    """Return a dictionary object of display name and data url as the key-value pairs.

    You want to look for the anchor tag and extract the info as follows:

        <a href="DATA_URL">DISPLAY_NAME</a>


    :param html_source:

        A sequence of characters (i.e., string) containing the html source to be parsed.

    """
    with open(html_source, "r", encoding="utf-8") as f:
        lines = f.read()

        url = re.compile('<a href="(.*?)">')  # DATA_URL 추출용 정규표현식 패턴
        name = re.compile('">(.*?)</a>')  # DISPLAY_NAME 추출용 정규표현식 패턴
        DATA_URL = url.findall(lines)
        DISPLAY_NAME = name.findall(lines)
        dict = {x: y for x, y in zip(DATA_URL, DISPLAY_NAME)}
        return dict


file = r"C:\Users\user\Downloads\test.txt"
result = data_url_extractor(file)
print(result)
