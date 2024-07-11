import random
random.randint(1,45)

# 1부터 45 사이에 랜덤 수 6개
i = 0
result = []
while i < 6 :
    i = i + 1
    result.append(random.randint(1,45))
print(result)

