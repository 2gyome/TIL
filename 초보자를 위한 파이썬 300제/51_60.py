#51. list 만들기
movie_rank = ["닥터 스트레인지","스플릿","럭키"]

#52. list에 원소 추가
movie_rank.append("배트맨")

#53. insert - 순서를 지정해서 널을 수 있음
movie_rank.insert(1,"슈퍼맨")

#54. 리스트 내 원소 삭제 - del
del movie_rank[3]

#55. 리스트 내 원소 여러개 삭제 - del
del movie_rank[2:]
print(movie_rank)

#56. 리스트 합
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang = lang1+lang2
print(lang)

#57. 리스트 내 최솟값, 최댓값
nums = [1, 2, 3, 4, 5, 6, 7]
print(min(nums), max(nums))

#58. 리스트의 합
print(sum(nums))

#59. 리스트 갯수
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#60. 리스트의 평균
print(sum(nums)/len(nums))
