x,y=list(map(int,input().split(":")))
angle=abs((30*x)-(11*y/2))
print(min(angle,360-angle))