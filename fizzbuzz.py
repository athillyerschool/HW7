def printFizzBuzz():
    for i in range(101):
        if(i%3 == 0 and i%5 != 0):
            print("Fizz")
        elif(i%3 != 0 and i%5 == 0):
            print("Buzz")
        elif(i%3 == 0 and i%5 == 0):
            #avoid printing FizzBuzz on 0
            if(i > 0):
                print("FizzBuzz")
        else:
            print(i)