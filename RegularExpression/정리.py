import re

# [] : [] 사이의 문자와 매치
# [a-zA-Z] : 모든 알파벳
# [0-9], [\d] : 모든 숫자
# a.b : a0b, aasdfdasb
# a[.]b : a.b
# ca*t : ct, cat, caat, caaat
# ca+t : cat, caat, caaat
# ca{2}t : caat
# ca{2,4}t : caat, caaat caaaat
# ab?c : ac, abc

# match : 문자열의 맨 앞부터 찾는다. 따라서 "babc"는 실패하고, "abc"는 성공한다.
p = re.compile("ab*")
m = p.match("babc")
print(m)
m = p.match("abc")
print(m)

# [출력 결과]
# None
# <re.Match object; span=(0, 2), match='ab'>

# search : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다. 중간에 포함되어도 찾아짐. 반환값은 match와 동일.
p = re.compile("python")
m = p.search("this is python regular expression")
print(m)

# [출력 결과]
# <re.Match object; span=(8, 14), match='python'>

# findall : 정규식과 매칭되는 모든 문자열(substring)을 리스트로 반환한다.
p = re.compile("[a-z]+")
m = p.findall("abc def gfg7daf77 22")
print(m)

# [출력 결과]
# ['abc', 'def', 'gfg', 'daf']


# match 객체의 메서드

# - group(): 매치된 문자열 반환
# - start(), end(): 시작과 끝 인덱스

# match 축약버전 제공.
# p = re.match("[a-z]+", "abc def")


# 컴파일 옵션
p = re.compile('a.b', re.DOTALL)
p = re.compile('[a-z]+', re.I)  # IGNORECASE

# Raw string
p = re.comple(r'\\section')
