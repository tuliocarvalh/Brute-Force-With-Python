import random
number = int(input("input password: "))
guess = 0
while (guess != number):
    guess = random.randint(0,9999)
    print(guess)
print("your password is " + str(guess))
