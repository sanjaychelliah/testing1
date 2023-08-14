#create a function to check prime numbers
def prime_check(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")