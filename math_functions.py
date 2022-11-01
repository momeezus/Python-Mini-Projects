def math_functions():
    arr = []
    num_list = int(input("How many values do you have?"))
    for i in range(num_list):
        number = float(input("Enter value number {0}".format(i+1)))
        arr.append(number)
    print("min =", min(arr))
    print("max =", max(arr))
    print("sum =", sum(arr))
    print("average =", sum(arr)/num_list)
math_functions()