## 무한하게 나열하고 싶은거
# contents = "사과"
# i = 0
# while contents == "사과":
#     print("그만해!")

i = 10
count = 0
while i < 100 :
    i = i + 1
    count = count + 1
    print("i는 지금 값이",i, "이므로, 100보다 작습니다.")
print(count)

# while문을 사용하여 대기번호를 출력하는 프로그램을 작성하시오. 최대 대기번호 발행수는 1000이다.(브레이크)
i = 0
while i < 1000 :
    i = i + 1
    if i == 500 :
        break
    print("대기번호 : ", i,"번 입니다.")

# while문을 사용하여 대기번호를 출력하는 프로그램을 작성하시오. 최대 대기번호 발행수는 1000이다.(else)
i = 0
while i < 1000 :
    i = i + 1
    print("대기번호 : ", i,"번 입니다.")
else :
    print("마감되었습니다. 죄송합니다.")
