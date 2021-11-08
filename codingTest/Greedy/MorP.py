S=input()
result=int(S[0])
# 0과 1일 때는 곱하는 것보다 더하는게 크므로 더해준다(문자열이므로 int형으로 바꿔줘야함)
# 나머지 경우에는 곱해준다
for i in range(1,len(S)):
  if S[i-1]=='0' or S[i]=='0' or S[i-1]=='1' or S[i]=='1':
    result+=int(S[i])
  else:
    result*=int(S[i])
print(result)
