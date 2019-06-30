a,b=map(int,input().split())
for i in range(a+1,b):
	sum=0
 	temp=0
	while(i>0):
		dig=i%10
                c=pow(dig,3)
		sum=sum+c
		i=i//10
		if(sum==temp):
			print(sum,end=' ')