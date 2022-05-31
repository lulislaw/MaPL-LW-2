x = int(input())
guess = 1
for i  in range(100):
    guess = (guess + (x / guess))/2
    print(i,guess)