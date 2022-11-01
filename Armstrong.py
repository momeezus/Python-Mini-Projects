def arm_strong():
    num = int(input('Enter an integer:'))
    i = num
    sum_num = 0
    power = len(str(num))
    while (i>0):
              last_digit = i % 10
              sum_num += last_digit**power
              i = i//10
    if num == sum_num:
              print(num, "is an Armstrong number.")
    else:
              print(num, "is not an Armstong number.")
arm_strong()