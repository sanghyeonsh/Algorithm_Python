N=int(input())
cnt=0
# 0시0분0초부터 N시59분59초까지이므로 첫 번째 반복문은 0~N까지 나머지는 0~59까지 분과 초를 나타내었다.
for i in range(N+1):
  for j in range(60):
    for k in range(60):
      if "3" in str(i)+str(j)+str(k):     #각 시분초를 문자열로 바꾸어 붙여주고 3인 안에 있는지의 여부를 확인한다.ㄴ
        cnt+=1
print(cnt)