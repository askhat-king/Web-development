n= int(input())
arr = list(map(int, input().split()))
a=0
for i in range(n):
	if(arr[i]>0):
		a+=1
print(a)