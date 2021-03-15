#리스트 = []
#튜플 = ()
#딕셔너리 = {}

e = [7, 4, 3,5,6,3,7,1]

e.sort(reverse=True)

e.insert(3, 7)

#print(e)



#e.append([3,4,5,6,7])
e.extend([3,4,5,6,7])
print(e)

#튜플 수정 불가능 그외에는 리스트랑 생성때 () 쓰는거 빼고는 다 비슷하다

#딕셔너리 Key, value

diction = {"name":"이해준", "age":21} #여러 자료를 다루기에 적합
print(diction["name"]) # == print(diction.get("name"))

popu = {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"} #각 종목별 유명한 사람들
#a1 = [사람 이름]
#a2 = [개인의 이름]

keys = popu.keys()
values = popu.values()

print('김연아' in popu)



#set = 수학에서 집합이랑 똑같습니다.
a = [1,2,3,3,3,4,5,6,6,7]
print(list(set(a)))


# | = shift + \


#define _CRT_SECURE_NO_WARNINGS

scanf // scanf_s

