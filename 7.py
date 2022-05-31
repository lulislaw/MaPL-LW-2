ces = str(input())
codeces = ""
for i in range(len(ces)):           #Только заглавные англ
    if((ord(ces[i]) != 88) and (ord(ces[i]) != 89) and (ord(ces[i]) != 90) and (ord(ces[i]) > 64) and (ord(ces[i]) < 91)):
        codeces = codeces + chr(ord(ces[i]) + 3)
    else:
        if(ord(ces[i]) == 88):
            codeces = codeces + chr(65)
        elif (ord(ces[i]) == 89):
            codeces = codeces + chr(66)
        elif (ord(ces[i]) == 90):
            codeces = codeces + chr(67)
        else:
            codeces = "error 0"
            break
print(codeces)