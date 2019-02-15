import random

print('1 20')

answer = random.randint(1, 20)
guess = 21

while guess != answer:
    guess = int(input('Write your number!'))
    if guess > answer:
        print('Less!')
    elif guess < answer:
        print('More!')
    else:
        print('Congratz!')
