#n,m,k 공백 구분 입력
n, m, k = map(int, input().split())
#n개의 수를 공백으로 구분하여 입력
data = list(map(int,input().split()))

data.sort()#정렬
first = data[n-1]#가장큰수 
second = data[n-2]

result=0

while True:
  for i in range(k):
    if m==0:
      break # m=0이면 탈출
    result += first
    m-=1
  if m==0:
    break
  result += second
  m -= 1
print(result)