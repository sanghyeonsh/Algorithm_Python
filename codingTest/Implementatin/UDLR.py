N=int(input())
arr=list(input().split())
x=1
y=1
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