__author__ = "Alex Li"

oldboy_age = 56
count = 0
while count < 3 :
    user_guess = int(input("input your guess num:") )
    if user_guess == oldboy_age:
        print("you got it!")
        break
    elif user_guess > oldboy_age:
        print("think smaller")
    else:
        print("think bigger")
    count += 1 #count++  count = count +1
else:
    print("你已经超过3次尝试了，笨蛋，fuck off!")
#if count == 3:
#    print("你已经超过3次尝试了，笨蛋，fuck off!")
#print('-------------------')