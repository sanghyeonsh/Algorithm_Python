N=int(input())
# 오름차순으로 해서 앞에서부터 확인해야 최댓값을 구할 수 있다.
arr=sorted(list(map(int,input().split())))
# cnt변수는 그룹마다 들어가는 모험가의 수를 담고 모험가수가 그룹내의 공포도최댓값보다 높거나 같아지면 그룹으로
# 하나 추가하고 그룹을 초기화해준다
cnt=0
group=0
for i in arr:
  cnt+=1
  if cnt>=i:
    group+=1
    cnt=0
print(group)