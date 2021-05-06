import random
import math


def main():
    count = 1
    n = int(input("Enter a number: "))
    secret_num = 42
    while True:
        if n > secret_num:
            print("The secret number is lower.")
            n = int(input("Enter a number: "))
        if n < secret_num:
            print("The secret number is higher")
            n = int(input("Enter a number: "))
        count += 1
        if n == secret_num:
            print("Correct!, it took you", str(count), " tries to guess it right.")
            break



if __name__ == '__main__':
    main()


