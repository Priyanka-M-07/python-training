import random

secret_number = random.randint(1, 10)
num = int(input("Enter the number: "))
while True:
    if num == secret_number:
        print("you are win")
        break
    elif num >= secret_number:
        print("num is low")
        break
    elif num <= secret_number:
        print("num is high")
        break