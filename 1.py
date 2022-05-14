arr = []
sum = 0
i = 1
k = 0
while i != 0:
    i = int(input())
    sum = sum + i
    k = k+1
if(sum == 0):
    print("error 0")
else:
    print("avg =", sum / (k-1))