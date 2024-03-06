#Ahmed Mohamed Ahmed  ID: 20231013
#Radwan Fouad Ahmed   ID: 20230138

#to check if the number is binary 
def checkbinary (number):
    return all(char in '01' for char in str(number))
#ones compelement function
def onescomplement (binarynumber):
    result = ""
    for i in range (0 , len(binarynumber)):
        if binarynumber[i] == '0':
            result += '1'
        elif binarynumber[i] == '1':
            result += '0'
    print(result)
#twos compelement function
def twoscompelment(binarynumber):
    result = ""
    for i in range (0 , len(binarynumber)):
        if binarynumber[i] == '0':
            result += '1'
        elif binarynumber[i] == '1':
            result += '0'
    carry = 1
    twoscompelment = ''
    for i in reversed(result):
        bits = int(i) + carry
        twoscompelment += str(bits % 2)
        carry = bits // 2
        if carry :
            twoscompelment += '1'
    twoscompelment = twoscompelment[::-1]
    print(twoscompelment)
# a function that chooses the biggest length between two numbers
def maximum_length (number1 , number2):
    if len(number1) > len(number2):
        return len(number1)
    elif len(number1) < len(number2):
        return len(number2)
    elif len(number1) == len(number2) :
        return len(number1)
# a function add zeroes to the least number in length so the operation of addition and subtraction can be done
def add_zeroes (number1 , number2):
    maximumlength = maximum_length(number1 , number2)
    number1 = number1.zfill(maximumlength)
    number2 = number2.zfill(maximumlength)
    return number1 , number2
#the addition function
def addition (number1 , number2):
    number1 , number2 = add_zeroes(number1 , number2)
    result = ""
    carry = 0
    i = len(number1) - 1
    while i >= 0 :
        sum = int(number1[i]) + int(number2[i]) + carry
        if sum == 0 :
            result += '0'
            carry = 0
        elif sum == 1:
            result += '1'
            carry = 0
        elif sum == 2 :
            result += '0'
            carry = 1
        elif sum == 3 :
            result += '1'
            carry = 1
        i -= 1
    if carry :
            result += '1'
    result = result[::-1]
    print(result)
#the subtraction function
def subtraction (number1 , number2):
    number1 , number2 = add_zeroes(number1 , number2)
    result = ""
    borrow = 0
    i = len(number1) - 1
    while i >= 0 :
        difference = int(number1[i]) - int(number2[i]) - borrow
        if difference == 0 :
            result += '0'
            borrow = 0
        elif difference == 1:
            result += '1'
            borrow = 0
        elif difference == -1 :
            result += '1'
            borrow = 1
        i -= 1
    result = result[::-1]
    print(result)
                              

menu1 = ("A" , "a" , "B" , "b")
menu2 = ("A", "a" , "B" , "b" , "C" , "c" , "D" , "d")
while True :
    while True :
        print("**binary calculator**")
        print("A) insert new numbers")
        print("B) Exit")
        user_input = input("please select an option: ")
        if user_input in menu1 :
            break
        else :
            print("please select a valid choice")
    if user_input == "A" or user_input == "a":
        binarynumber = input("enter a new number")
        if checkbinary(binarynumber) :
            while True :
                print("**please select an operation**")
                print("A) compute one's complement")
                print("B) compute two's complement")
                print("C) addition")
                print("D) subtraction")
                user_2input = input("please select an option: ")
                if user_2input in menu2 :
                    break
                else :
                    print("please select a valid option")
            if user_2input == "A" or user_2input == "a":
                print(onescomplement(binarynumber))
            elif user_2input == "B" or user_2input == "b":
                print(twoscompelment(binarynumber))
            elif user_2input == "C" or user_2input == "c":
                seconedbinarynumber = input("enter the number you want to add")
                if checkbinary(seconedbinarynumber):
                    print(addition(binarynumber , seconedbinarynumber))
                else :
                    print ("the number you enterd is not binary")
            elif user_2input == "D" or user_2input == "d":
                seconedbinarynumber = input("enter the number you want to subtract")
                if checkbinary(seconedbinarynumber):
                    print(subtraction(binarynumber , seconedbinarynumber))
                else :
                    print("the number you entered is not binary")
        else:
            print (binarynumber , "is not a binary number")
    elif user_input == "B" or user_input == "b":
        print("thank you for using binary calculator")
        break

    
