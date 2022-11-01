def arm_stronginrange():
    for num in range(int(input("Enter the max value of your range (min = 0)."))):
        power = len(str(num))
        sum_num = 0
        i = num
        while (i>0):
                  last_digit = i % 10
                  sum_num += last_digit**power
                  i = i//10
        if num == sum_num:
            print(num, "is an Armstrong number.")
        #else:
            #print(num, "is NOT an Armstrong number.")
arm_stronginrange()
