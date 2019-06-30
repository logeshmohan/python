n=int(input())
L=list(map(int,input().split()))
max1=L[0]
for i in range(n):
	if L[i]> max1:
		max1=L[i]
		print(max1)