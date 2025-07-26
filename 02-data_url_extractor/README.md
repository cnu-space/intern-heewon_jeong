# Usage

아래와 같이 `argparse` 모듈을 사용하면 명령 프롬프트를 통해 필요한 인자들을 입력받을 수 있다.

```python
import argparse
parser = argparse.ArgumentParser(
                    prog='data_url_extractor',
                    description='Which files matches the search options')
parser.add_argument('html_source', help = 'A sequence of characters (i.e., string) containing the html source to be parsed.')
parser.add_argument('--probe')
parser.add_argument('--inst')
...
parser.add_argument('--ver')

args = parser.parse_args()
# --로 시작하는 선택적 인자들 중 실제로 입력된 것들만 딕셔너리 객체로 만들어서 키워드 인수 param으로 함수에 전달
param = {k:v for k, v in vars(args).items() if k != 'html_source' and v is not None}
```

Shell prompt에 다음과 같이 실행한다.

```sh
python data_url_extractor.py C:\Users\user\Downloads\html_source.txt --probe rbsp-a --inst magnetometer --date 20160112
```
