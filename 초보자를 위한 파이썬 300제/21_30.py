#21 문자열 인덱싱
letters = 'python'
print(letters[0], letters[2])

#22. 슬라이싱 [시작인덱스 : 끝 인덱스 : 오프셋(간격)]
string = "홀짝홀짝홀짝"
print(string[::2])

#23. 인덱싱 시, 시작은 0
license_plate = "24가 2210"
print(license_plate[-4::])

#24. 거꾸로 출력 - 0부터 해도 0은 포함 안되네.. 뭐징
string = "PYTHON"
print(string[::-1])

#25.문자열 치환 - split 사용하면 string 이 되어 정답을 만족 못함 -> - --> 공백으로
phone_number = '010-1111-2222'
phone_number2 = phone_number.replace("-", " ")
print(phone_number2)

#26.
phone_number3 = phone_number.replace("-", "")
print(phone_number3)

#27. 마지막 도메인만 가져오고싶으면 . 뒤에것을 가져오면된다
url = "http://sharebook.kr"
url2 = url.split(".")
print(url2[-1])

#28. 문자열은 불변하다
lang = "python"
# lang[0] = 'P' --> 문자열은 할당 메서드를 지원하지 않는다.

#29. replace 매서드 소문자 a를 대문자로 변경
string = 'abcdef2a354a32a'
print(string.replace('a', 'A'))

#30. replace 메서드 --> 원본은 바뀌지 않고 새로운 문자열 객체로 리턴한다
string = 'abcd'
string.replace('b', 'B')
print(string)

