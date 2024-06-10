# PW



def prime_checker(number):
    if number == 1:
        print("It's not a Prime number")
    elif number == 2 or number == 3 or number == 5 or number % 7 == 0:
        print("It's a Prime number.")
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        print("It's not a Prime number")
    else:
        print("It's a Prime number")


# VID



def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a Prime number")
    else:
        print("It's not a Prime number")



n = int(input("Check this number: "))
prime_checker(number=n)
