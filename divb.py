a=int(input())
b=int(input())
i=1
while True:
    if (i%a==0) and (i%b==0):
        print(i)
        break
    else:
        i=i+1
    
