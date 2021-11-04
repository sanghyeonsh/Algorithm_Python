data=input()
row=int(data[1])
column=int(ord(data[0]))-int(ord("a"))+1
# 나이트가 이동가능한 모든 방법을 knight배열 안에 넣어주었다.
knight=[[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
sum=0
#체스판 밖으로 벗어나는 경우를 제외하고 모두 세주었다.ㄴ
for i in range(8):
  if row+knight[i][0]>=1 and row+knight[i][0]<=8 and column+knight[i][1]>=1 and column+knight[i][1]<=8:
    sum+=1
print(sum)