import math

prevX = 0
prevY = 0
print("Введите первую координату X:")
x = float(input())
print("Введите первую координату Y:")
y = float(input())
empty = ""
line = 0
sum = 0
sX = "x"
sY = "y"
while (sX != empty) and (sY != empty):
    print("Введите следующую координату X (Enter для окончания ввода):")
    prevX = x
    sX = str(input())
    if(sX == empty):
        break
    else:
        x = int(sX)
    print("Введите координату Y(Enter для окончания ввода):")
    prevY = y
    sY = str(input())
    if (sY == empty):
        break
    else:
        y = int(sY)
    line = math.sqrt((prevX - x)**2 + (prevY - y)**2)
    sum = sum + line

print("Периметр многоугольника равен", sum)
