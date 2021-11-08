N,K=map(int,input().split())
cnt=0
#나눠질 때는 무조건 나눠지는게 빠르므로 나누고 안나눠지면 나눠지도록 -1을 해준다
while True:
  if N==1:
    break
  else:
    if N%K==0:
      N/=K
      cnt+=1
    else:
      N-=1
      cnt+=1
print(cnt)