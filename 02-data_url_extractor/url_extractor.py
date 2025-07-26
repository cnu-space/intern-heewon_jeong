# step3
def url_extractor(latest, **param):
    """
    DESCRIPTION
        조건을 만족하는 url들의 집합를 반환하는 함수

    PARAMETER
        latest: 최신 버전 파일들의 속성(i.e. 네임드튜플)을 키로 하고 url을 값으로 갖는 딕셔너리
                (함수 update()의 반환값)
        param: 사용자로부터 입력받은 키워드 인수
               검색 옵션과 내용을 각각 키와 값으로 한다
               e.g. {'probe' : 'rbsp-a', 'res':'4sec-gsm', ...}

    FUNCTION
        _set(**param): 매칭되는 url들을 묶어놓은 집합들을 각 옵션마다 구하고, 그 집합들로 구성된 리스트를 반환함
        intersect(set_list): 리스트에 포함된 세트들 전체의 교집합을 반환함
    """

    def _set(**param):
        set_list = []
        for option in param:  # option: param의 key
            s = {
                latest[ntk]
                for ntk in latest.keys()
                if ntk._asdict()[option] == param[option]
            }
            set_list.append(s)
        return set_list

    def intersect(set_list):
        result = set_list[0].intersection(*set_list)
        return result

    return intersect(_set(**param))
