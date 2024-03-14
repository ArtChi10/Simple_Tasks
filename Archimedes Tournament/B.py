n, m = map(int, input().split())
a = [int(i) for i in input().split()]
a = a*2
BestNews = -1
ShortOfNewsline = 10**7
for k in range(n):
    SumOfJoy = 0
    count = 0
    for i in range(k, k+n):
        SumOfJoy = SumOfJoy+a[i]
        count+=1
        if SumOfJoy>=m and count<ShortOfNewsline:
            BestNews = k
            ShortOfNewsline = count
if BestNews !=-1:
    print(BestNews+1, ShortOfNewsline)
else:
    print("-1")
