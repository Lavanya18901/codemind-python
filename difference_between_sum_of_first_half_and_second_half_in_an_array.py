n=int(input())
arr=list(map(int,input().split()))
sof=0
sos=0
for i in range(n):
  if(i<n//2):
      sof+=arr[i]
  else:
      sos+=arr[i]
print(abs(sof-sos))