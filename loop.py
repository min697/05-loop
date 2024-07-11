
# for /

var = [1,2,3]

if 3 in var :
    print("원하는 숫자가 있습니다.")
else :
    print("찾으시는 숫자가 없습니다.")

fruits = ['사과', '바나나', '딸기']

for var in fruits :
    print("이는 첫번째 코드블록 라인입니다.", var)
    print("이는 두번째 코드블록 라인입니다.", var)
print("이는 for 반복문의 코드블록입니다.")

# dic 반복문
dic ={"봄":"숭어", "여름":"수박", "숫자": 3}
for var in dic :
# dic 은 key가 중심이기 때문에
#     print(var)
#  고치고싶은게 value 값을 구하고 싶을 때는
    print(var, dic[var])


