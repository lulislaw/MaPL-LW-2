plali = str(input())
count = 0
for i in range(len(plali) // 2):
    if(plali[i] == plali[len(plali)-1-i]):
        count = count + 1
if(count == (len(plali)//2)):
    print("Палиндром")
else:
    print("Не палиндром")
    # Регистр учитываеться