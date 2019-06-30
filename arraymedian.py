n=int(input())
L=list(map(int,input().split()))
s=sorted(L)
print(s)
k=len(s)
r=k//2
if k%2==1:
	med=s[r]
	print(med)
else:
	med=(s[r-1]+s[r])/2
	print(med)