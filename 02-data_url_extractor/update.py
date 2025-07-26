# step2
from collections import namedtuple

name = namedtuple("name", "probe, inst, res, prod, date, ver")


def update(parsed):
    """
    DESCRIPTION
        파일들의 속성(i.e. 네임드튜플)과 url을 키-값 쌍으로 하는 딕셔너리
        이때 딕셔너리는 각 날짜에 대한 최신 버전 파일으로만 구성됨

    PARAMETER
        parsed: 파일명, url 쌍으로 이루어진 딕셔너리
                (함수 name_url()의 반환값)
    """
    ntparsed = {}
    for k, v in parsed.items():
        tk = k.split("_")
        if len(tk) == 6:  # 'Name', 'Last modified', 'Size', ... 제외
            ntk = name._make(tk)  # ntk = name(probe='rbsp-a',..., ver='v1.3.3.cdf')
            # ntparsed = {name(probe='rbsp-a',..., ver='v1.3.3.cdf') : 'rbsp-a_..._v1.3.3.cdf', ...}
            ntparsed[ntk] = v

    # item[0].date = name.date = '2016xxxx' / item[0].ver = name.ver = 'v~~.cdf'
    sort = dict(sorted(ntparsed.items(), key=lambda item: (item[0].date, item[0].ver)))
    sorted_keys = {k.date: k for k in sort.keys()}

    latest = {key: sort[key] for key in sorted_keys.values()}
    return latest


# _make(), _asdict(): namedtuple의 메소드 (파이썬 공식 튜토리얼에서 확인할 수 있다)
