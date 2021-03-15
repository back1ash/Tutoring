ten = 10
seven = 7
eight = 8


print("ten에 저장된 숫자는 ten입니다.")
print(f"각각 변수들에 저장된 숫자는 {ten},{seven},{eight}입니다.\n\n\n")

#자릿수

PI = 3.14159265359
print("%0.7f" %PI)

string = "위에서 보았듯이"

print("%-10s" %string)

string = "문자열 중 문!자 b가 : 처음으로 나온 !위치를 : 반환한다. 만약 찾는 문자나 문자!열이 존재하지 않는다면 -1을 반환한다."

print(f"{string.find('문')}")

a = ",".join('abcd')
print(a)

b = string.split(":")

print(b)