data=input()
row=int(data[1])
column=int(ord(data[0]))-int(ord("a"))+1

knight=[[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
sum=0
for i in range(8):
  if row+knight[i][0]>=1 and row+knight[i][0]<=8 and column+knight[i][1]>=1 and column+knight[i][1]<=8:
    sum+=1
print(sum)