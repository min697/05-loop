# while문을 사용하여 1부터 100까지 수/ i 변수가 하는 역할 = 조건문일 때 조건을
# 제어하기 위함 (for은 기준이 있었음)
index = 1
# result 하는 역할 : 연산 결과 값을 저장
result = 0
while index < 100:
    index = index + 1
# 홀수 인지 확인
    if index % 2 == 1:
# 홀수라면 그 값을 저장
        result = result + index
# 나온 수의 합
print(result)