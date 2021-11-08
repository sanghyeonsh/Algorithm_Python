N=int(input())
cnt=0
arr=[500,100,50,10]
# 500,100,50,10순으로 몫은 개수로 나머지는 다음동전으로 넘긴다.
for i in arr:
  cnt+=N//i
  N=N%i
print(cnt)