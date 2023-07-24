
# 정규표현식
# re 모듈 1. match: 무조건 문자열 가장 앞에 일치하는지 검사 후 매칭
import re
from tokenize import group
print(re.match('hello', 'hello, world!')) # <re.Match object; span=(0, 5), match='hello'>
print(re.match('a', 'abcdefg')) # <re.Match object; span=(0, 1), match='a'> #abcdefg에서 a가 첫번째로 매칭됨
print(re.match('a', 'abcabc')) # <re.Match object; span=(0, 1), match='a'> #abcabc 중 가장 첫번째인 a로 반환됨 위치도 0,1
print(re.match('a', 'bbb')) #None
print(re.match('a', 'bae')) #None #a가 들어있지만 처음부터 시작되지 않아 None

# match object의 메소드
text = 'I would describe myself as an extrovert'
pattern = 'extrovert'

G = re.search(pattern, text).group()
Start = re.search(pattern, text).start()
E = re.search(pattern, text).end()
Span = re.search(pattern, text).span()

print('group의 결과:', G)
print(f'start의 결과: {Start}')
print('end의 결과: {0}'.format(E))
print('span의 결과: {}'.format(Span))

# re 모듈 2. search : 문자열 전체 검사 후 일치하는 것 중 첫번째를 매칭
sentence = 'Individuals unconsciously associate other people with themselves.'
result = re.search("associate", sentence)
what = re.search("associate", sentence).group()
S = re.search("associate", sentence).start()
E = re.search("associate", sentence).end()
span = re.search("associate", sentence).span()
print(f"찾은것: {what} 결과: {result}" )
print("시작 위치: {0}\n끝위치: {1}\n시작&끝 위치: {2}".format(S, E, span))

# re 모듈 3. findall : 일치하는 모든 문자열(패턴)을 찾아 리스트로 반환
findall_text = "가로 시작하는 말은 가위, 가장, 가수, 가지"
a = re.findall("가", findall_text)
가_length = len(a)
print(f"findall의 결과: {a}\n\"가\"가 들어간 횟수: {가_length}")

# re 모듈 4. finditer: 반복가능객체 iterator object를 반환
import re
p = re.compile('[a-z]+')
result = p.finditer("life is too short")
print(result) # <callable_iterator object at 0x00000257904D34F0>

for a in result: print(a)

# 반복 가능한 객체가 포함하는 각각의 요소는 match 객체

# re 모듈 5. fullmatch: 패턴과 전부 완벽하게 매치하는가를 조사 안되면 None 반환
import re
site = input("메일 입력: ")
m = re.fullmatch(r'[a-zA-Z0-9]+@[a-z]+\.com', site)
print(m)

# re 모듈 6. sub: 일치된 패턴을 다른 문자로 대체
text = 'I would describe myself as an extrovert'
pattern = 'extrovert'
extrovert = re.search(pattern, text)
introvert = re.sub(pattern, "introvert", text)
print("바꾸기 전: ", text)
print("sub 결과: ", introvert)

# re 모듈 7. split: 패턴 기준으로 문자열을 나눠 리스트로 반환
Hyebin = "유아교육과,취준생,기타연주,피아노연주,독서,배드민턴,카메라,아이들,파이썬입문기"
result = re.split(",", Hyebin)
print(f"윤혜빈을 나타내는 것들: \n{result}")

# 이메일 주소 찾기 (이메일 주소를 나눠 리스트 요소로 넣기)
email = input("이메일 주소 입력(,로 구분): ")
s = "저의 이메일 주소는 hyeshinoh@gmail.com입니다. 또한 panda706@naver.com도 가지고 있습니다."
e_pattern = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com'
address = re.findall(e_pattern, email)
print(address)

# # 주민등록번호 뒷자리를 *******로 변경하기
data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

# 다음 소스 코드를 완성하여 주어진 이메일 주소가 올바른지 판단하도록 만드세요. emails 리스트에서 앞의 다섯 개는 올바른 형식이며 마지막 세 개는 잘못된 형식입니다.

# practice_regular_expression.py
import re

p = re.compile('[a-zA-Z0-9]+[~!@#$%^&*>_-]*@[a-zA-Z].[a-z]+')
emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식
 
for email in emails:
    print(p.match(email) != None, end=' ')

a = re.compile('love') #compile은 패턴을 정의함
print(type(a))
print(a.findall("i love you"))