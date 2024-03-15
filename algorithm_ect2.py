# 투 포인터
# 리스트에 순차적을 접근해야할때 2개의 점의 위치를 기록하면서 처리하는 알고리즘

#특정한 합을 가지는 부분 연속 수열 찾기
n=5 # 데이터의 개수
m=5 # 찾고자 하는 부분합 M
data=[1,2,3,4,5]  # 전체수열

count=0
interval_sum=0
end=0

#start를 차례로 증가시키며 반복
for start in range(n):
    while interval_sum < m and end <n: # end를 가능한 만큼 이동시키기
        interval_sum +=data[end] # 연속된 수열
        end+=1

    if interval_sum==m: # 부분합이 m일때 카운트 증가
        count+=1
    interval_sum -=data[start] #다음수열로 넘어가기

print(count)


# 투 포인터 - 정렬되어있는 두 리스트의 합집합

#사전에 정렬된 리스트 a,b선언
n, m = 3,4
a=[1,3,5]
b=[2,4,6,8]

result=[0]*(n+m)
i=0
j=0
k=0

while i < n or j<m:
    if j>m or(i<n and a[i]<=b[j]):
        result[k]=a[i]
        i+=1
    else:
        result[k]=b[j]
        j+=1
    k+=1

for i in result:
    print(i,end=" ")



# 구간합계산

ㅜ=5