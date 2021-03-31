n= int(input())
arr = list(map(int, input().split()))
a=0
for i in range(1, n-1):
	if ((arr[i]<0) and (arr[i+1]<0)) or ((arr[i]>0) and (arr[i+1]>0)):
		a=1
if(a==1):
	print('YES')
else:
	print('NO')