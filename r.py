import random
r = random.randint(1, 100) 
time = 0

while True:
    time += 1    # time = time + 1
    guess=input('請猜一個數字:')
    guess=int(guess)
    if guess == r:
        print('你猜對了!')
        break

    elif guess > r :
        print ('比答案大')
    elif guess < r :
        print ('比答案小')
    print('這是你猜的第',time, '次')
    
#randint隨機整數 
#module 模組 =一個python檔案
#package = 套件 很多檔案