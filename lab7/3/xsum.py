a = int(input())
sum=0
while a>0:
	mod=a%10
	sum=sum+mod
	a=a//10
print(sum)