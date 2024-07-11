# 사용자가 입력한 수가 3의 배수이면 ok 출력하는 프로그램 작성하시오
num = int(input("임의의 수를 입력하세요"))
if num % 3 == 0:
    print("ok")
# 그렇지 않으면 no 출력
else :
    print("no")

# 리스트가 있다
numbers = [100,200,300]
# 부가세가 포함된 가격을 for 문을 사용해서
for plus_numbers in numbers :
    result = int(plus_numbers * 1.1)
    print(result)
# 화면에 출력 단 부가세는 10%으로 가정

