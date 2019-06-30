n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
	if i==l[i]:
		a.append(i)
iflen(a)>=1:
	print(*a)
else:
	print(-1)