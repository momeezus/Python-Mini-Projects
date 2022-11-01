def prime_finder():
    num = int(input("Enter an integer:"))
    for divisor in range (2, num):
        if num % divisor == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
            
prime_finder()