N=int(input())
arr=list(input().split())
x=1
y=1
# 배열의 각 요소마다 상하좌우에 따라 +=1을 해주고 정사각형을 벗어나는 경우에는 제자리에 두었다.
for i in arr:
  if i=="U" and x!=1:
    x-=1
  elif i=="D" and x!=N:
    x+=1
  elif i=="L" and y!=1:
    y-=1
  elif i=="R" and y!=N:
    y+=1
print(x,y)