n=int(input())
m=list(map(int,input().split()))
s=0
for i in range(n):
    s+=m[i]
    o=s//n
if o in m:
    print("True")
else:
    print("False")