# p.468
#소수 판별 알고리즘

import math

def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수를 확인 -> 가운데 약수까지만 나누어떨어지는지 확인
    for i in range(math.sqrt(x)+1):
        #x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))


# p.471
# 에라토스테네스 채 알고리즘 -> 여러개의 수가 소수인지 판별

import math

n=1000  # 2~1000 모든수에 대해 소수 판별
array=[True for i in range(n+1)] # 처음엔 모든 수가 소수인것으로 초기화

for i in range(2,int(math.sqrt(n))+1):
    if array[i] == True: #i가 소수인 경우
        
        #i를 제외한 i의 모든 배수를 지우기
        j=2
        while i*j <=n:
            array[i*j]=False
            j+=1

#모든 소수 출력
for i in range(2,n+1):
    if array[i]:
        print(i,end=' ')



