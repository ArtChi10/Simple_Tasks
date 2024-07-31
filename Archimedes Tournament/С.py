n = int(input())
t = int(input())
a = []
if t<-(10**9) or t>10**9:
    print("NO")
else:
    for i in range(1, 101):
        a.append(i)
        k = - i
        a.append(k)
    b = [0]*n
    for i in range(len(b)-1):
        b[i]=a[i]
    b[-1]=t-sum(b)
    s=''
    for i in range(len(b)-1):
        s = s+str(b[i])+" "
    s = s + str(b[-1])
    print("YES")
    print(s)