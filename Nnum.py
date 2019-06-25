q=int(input())
n=list(map(int,input().split()))
l=[]
for x in range(q):
    for i in range(x+1,len(n)):
        if(n[i]==n[x]):
          lio.append(n[x])

if (len(l)==0):
    print("unique")
else:
    l.sort()
    li2=set(l)
    for x in li2:
        print(x,end=" ")