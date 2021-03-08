def checkLeap(number):
    if(number%400 == 0):
        return "leapyear"
    if(number%100 == 0):
        return "not leapyear"