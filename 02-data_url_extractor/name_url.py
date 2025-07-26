# step1
def name_url(html_source):
    """
    DESCRIPTION
        Return a dictionary object of display name and data url as the key-value pairs.
        You want to look for the anchor tag and extract the info as follows:
            <a href="DATA_URL">DISPLAY_NAME</a>

    PARAMETER
        html_source: A sequence of characters (i.e., string) containing the html source to be parsed.
                     (HTML 소스의 파일 주소를 입력한다)
    """
    parsed = {}
    with open(html_source, "r", encoding="utf-8") as f:
        while True:
            i = 0
            line = f.readline().strip()
            if not line:
                break
            else:
                while i < len(line):
                    text = ""
                    if line[i : i + 3] == "<a ":
                        i = i + 3  # <a 건너뛰기
                        if line[i : i + 6] == 'href="':
                            k = i + 6  # href=" 건너뛰기
                            while line[k : k + 4] != "</a>":
                                if k < len(line):
                                    text += line[k]
                                    k += 1
                                else:
                                    break
                            else:
                                x = text.split('">')
                                parsed[x[1]] = x[0]  # x[1]: name / x[0]: url
                                i = k + 4  # </a> 건너뛰기
                    else:
                        i += 1  # <a 없으면 다음 글자로
    return parsed


# 만약 line의 길이가 슬라이싱한 길이보다 작더라도 오류가 발생하는 대신 다음 line으로 넘어간다.
