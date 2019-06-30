import sys
import math
hr1,mins1=map(int,input().split(':'))
hr2,mins2=map(int,input().split(':'))
hr=abs(hr2-hr1)
mins=abs(mins2-mins1)
print(hr,'hrs',mins,'mins')