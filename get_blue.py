for _ in range(int(input())):
  l,r=map(int,input().split())
  s=input();
  l1,l2,r1,r2=0,0,0,0
  for i in s:
    if i=='U':r1+=1
    if i=='D':r2+=1
    if i=='R':l1+=1
    if i=='L':l2+=1
  flag=False;flag1=False
  if l>=0 and l1>=l:flag=True
  if l<=0 and l2>=abs(l):flag=True
  if r>=0 and  r1>=r:flag1=True
  if r<=0 and r2>=abs(r):flag1=True
  if flag and flag1:print("YES")
  else:print("NO")
