n= int(input())
arr = list(map(int, input().split()))
a=0
for i in range(1,n):
	if(arr[i]>arr[i-1]):
		a+=1
print(a)