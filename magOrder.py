def mag_order():
    integer = int(input('Enter an integer no more than 3-digits long'))
    hundreds = int(integer/100)
    tens = int((integer - hundreds*100)/10)
    units = int(integer - hundreds*100 - tens*10)
    print ("The hundred’s digit of your number is:", hundreds)
    print ("The ten’s digit of your number is:", tens)
    print ("The unit’s digit of your number is:", units)
mag_order()