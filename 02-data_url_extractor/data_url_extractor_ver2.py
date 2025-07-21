def data_url_extractor(html_source, **param):

    from collections import namedtuple

    # import sys
    # import argparse

    with open(html_source, "r", encoding="utf-8") as f:
        parsed = {}
        while True:
            i = 0
            line = f.readline().strip()
            if not line:
                break
            else:
                while i < len(line):
                    text = ""
                    if line[i : i + 3] == "<a ":
                        i = i + 3  # <a  건너뛰기
                        if line[i : i + 6] == 'href="':
                            i = i + 6  # href=" 건너뛰기
                            while line[i : i + 4] != "</a>":
                                text += line[i]
                                i += 1
                            else:
                                x = text.split('">')
                                parsed[x[1]] = x[0]
                                i = i + 4  # </a> 건너뛰기
                        else:
                            i += 1  # href=" 없으면 다음 글자로
                    else:
                        i += 1  # <a  없으면 다음 글자로
    # return parsed

    name = namedtuple("name", "probe, inst, res, prod, date, ver")
    ntparsed = {}
    for k, v in parsed.items():
        ntk = name._make(
            k.split("_")
        )  # ntk = name(probe='rbsp-a',..., ver='v1.3.3.cdf')
        # ntparsed = {name(probe='rbsp-a',..., ver='v1.3.3.cdf') : 'rbsp-a_..._v1.3.3.cdf', ...}
        ntparsed[ntk] = v
    # return ntparsed

    sort = sorted(ntparsed.items(), key=lambda x: x[0].ver, reverse=True)
    sort = dict(sorted(sort, key=lambda x: x[0].date))
    # x[0].ver = name.ver = 'v~~.cdf' / x[0].ver = name.date = '2016xxxx'
    # return sort

    latest = {}
    for k, v in sort.items():
        if not list(latest.keys()):
            latest[k] = v
        elif not k.date in list(latest.keys())[-1]:
            latest[k] = v
        else:
            continue
    # return latest

    for key in param.keys():  # key = 'probe', 'res', 'inst' ...
        url = []
        for k, v in latest.items():
            # k = name(probe='',..., ver=''), name(probe='',..., ver=''), ...
            # v = 'rbsp-a_..._v1.3.3.cdf', 'rbsp-a_..._v1.3.5.cdf', ...
            if param[key] == k._asdict()[key]:
                url.append(v)
    return url
