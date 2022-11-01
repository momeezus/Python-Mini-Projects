def bubbleSort():
    path = input("Enter the path to your file...")
    myFile = open(path, 'r')
    lines = myFile.readline().split()
    arr = []
    while lines:
        for number in lines:
            number = int(number)
            arr.append(number)
        lines = myFile.readline().split()
    print('Your unsorted array is: ', arr)
    for numbers in range(len(arr)):
        for sortedDigit in range(0, len(arr) - 1):
            if arr[sortedDigit] > arr[sortedDigit+1]:
                temp = arr[sortedDigit]
                arr[sortedDigit] = arr[sortedDigit+1]
                arr[sortedDigit + 1] = temp
    print('Your sorted array is: ', arr)
bubbleSort()