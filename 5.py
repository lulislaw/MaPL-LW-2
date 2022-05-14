print("Ввод(до 8 значений)(0/1):")
st = "1"
while(st != ""):
    st = str(input())
    if(len(st) > 0):
        if(len(st) != 8):
            st= "0" * (8 - len(st)) + st
            print(st)
        if(st.count("1") + st.count("0") == 8):
            if(st.count("1") % 2 == 0):
                print("0")
            else:
                print("1")
        else:
            print("Неверное значение")
    else:
        break