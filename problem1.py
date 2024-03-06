#Ahmed Mohamed Ahmed  ID: 20231013
#Radwan Fouad Ahmed   ID: 20230138

# checkhexadecimal is a function that check the number entered is hexadecimal
def checkhexadecimal (number):
    return all(char in '0123456789ABCDEFabcdef'for char in str(number))
# checdecimal is a function that check the number entered is decimal
def checkdecimal (number):
    return all(char in '0123456789'for char in str(number) )
# checkbinary is a function that check the number entered is binary
def checkbinary (number):
    return all(char in '01'for char in str(number))
# checkoctal is a function that check the number entered is octal
def checkoctal (number):
    return all(char in '01234567'for char in str(number))
# decimal to binary is a function that converts the decimal number entered by the user to binary 
def decimaltobinary(number):
    number = int(number)
    binarynumber = i =0
    while (number!=0):
        binarynumber = binarynumber + (number%2)*(10**i)
        number = number//2
        i+=1
    print(binarynumber)
# decimal to octal is a function that converts the decimal number entered by the user to octal 
def decimaltooctal(number):
    number = int(number)
    octalnumber = i =0
    while (number!=0):
        octalnumber = octalnumber + (number%8)*(10**i)
        number = number//8
        i+=1
    print(octalnumber)
# binary to decimal is a function that converts the binary number entered by the user to decimal 
def binarytodecimal (number):
    number = int(number)
    decimalnumber = i =0
    while (number!=0):
        decimalnumber = decimalnumber + (number%10)*(2**i)
        number = number//10
        i+=1
    print(decimalnumber)
# binary to octal is a function that converts the binary number entered by the user to octal 
def binarytooctal (number):
    number = int(number)
    decimalnumber = i =0
    while (number!=0):
        decimalnumber = decimalnumber + (number%10)*(2**i)
        number = number//10
        i+=1
    j = octalnumber = 0
    while decimalnumber > 0:
        octalnumber = octalnumber + (decimalnumber % 8)*(10**j)
        decimalnumber = decimalnumber // 8
        j += 1
    print(octalnumber)
# octal to decimal is a function that converts the octal number entered by the user to decimal 
def octaltodecimal (number):
    number = int(number)
    decimalnumber = i =0
    while (number!=0):
        decimalnumber = decimalnumber + (number%10)*(8**i)
        number = number//10
        i+=1
    print(decimalnumber)
# octal to binary is a function that converts the octal number entered by the user to binary 
def octaltobinary (number):
    number = int(number)
    decimalnumber = i =0
    while (number!=0):
        decimalnumber = decimalnumber + (number%10)*(8**i)
        number = number//10
        i+=1
    j = binarynumber = 0
    while decimalnumber > 0:
        binarynumber = binarynumber + (decimalnumber % 2)*(10**j)
        decimalnumber = decimalnumber // 2
        j += 1
    print(binarynumber)
# decimal to hexadecimal is a function that converts the decimal number entered by the user to hexadecimal 
def decimaltohexadecimal (number):
    number = int(number)
    hexadecimal_dictionary = "0123456789ABCDEF"
    if number == 0:
        return 0
    hexadecimalnumber = ""
    while number > 0:
        remainder = number%16
        hexadecimalnumber = hexadecimal_dictionary[remainder]+hexadecimalnumber
        number = number//16
    return hexadecimalnumber
# binary to hexadecimal is a function that converts the binary number entered by the user to hexadecimal 
def binarytohexadecimal (number):
    number = int(number)
    decimalnumber = i = 0
    while number != 0:
        decimalnumber = decimalnumber + (number%10)*(2**i)
        number = number//10
        i += 1
    hexadecimalnumber = decimaltohexadecimal(number)
    print(hexadecimalnumber)
# octal to hexadecimal is a function that converts the octal number entered by the user to hexadecimal 
def octaltohexadecimal (number):
    number = int(number)
    decimalnumber = i = 0
    while number != 0:
        decimalnumber = decimalnumber + (number%10)*(8**i)
        number = number//10
        i += 1
    hexadecimalnumber = decimaltohexadecimal(number)
    print(hexadecimalnumber)
# hexadecimal to decimal is a function that converts the hexadecimal number entered by the user to decimal 
def hexadecimaltodecimal (number):
    hexadecimalcharacters = "0123456789ABCDEF"
    decimalnumber = 0
    number = str(number)
    hexadecimallength = len(number)
    for i in range(hexadecimallength):
        digit = number[i]
        if digit in hexadecimalcharacters :
            counter = 0
            while counter < len(hexadecimalcharacters) and digit != hexadecimalcharacters[counter]:
                counter = counter + 1
            if counter < len(hexadecimalcharacters):
                power = 1
                for i in range (hexadecimallength-1-i):
                    power = power * 16
                decimalnumber += counter * power
    print(decimalnumber)
# hexadecimal to binary is a function that converts the hexadecimal number entered by the user to binary 
def hexadecimaltobinary (number):
    hexadecimalcharacters = "0123456789ABCDEF"
    decimalnumber = 0
    number = str(number)
    hexadecimallength = len(number)
    for i in range(hexadecimallength):
        digit = number[i]
        if digit in hexadecimalcharacters :
            counter = 0
            while counter < len(hexadecimalcharacters) and digit != hexadecimalcharacters[counter]:
                counter = counter + 1
            if counter < len(hexadecimalcharacters):
                power = 1
                for i in range (hexadecimallength-1-i):
                    power = power * 16
                decimalnumber += counter * power
    decimalnumber = int(decimalnumber)
    binarynumber = j =0
    while (decimalnumber!=0):
        binarynumber = binarynumber + (decimalnumber%2)*(10**j)
        decimalnumber = decimalnumber//2
        j+=1
    print(binarynumber)
# hexadecimal to octal is a function that converts the hexadecimal number entered by the user to octal 
def hexadecimaltooctal (number):
    hexadecimalcharacters = "0123456789ABCDEF"
    decimalnumber = 0
    number = str(number)
    hexadecimallength = len(number)
    for i in range(hexadecimallength):
        digit = number[i]
        if digit in hexadecimalcharacters :
            counter = 0
            while counter < len(hexadecimalcharacters) and digit != hexadecimalcharacters[counter]:
                counter = counter + 1
            if counter < len(hexadecimalcharacters):
                power = 1
                for i in range (hexadecimallength-1-i):
                    power = power * 16
                decimalnumber += counter * power
    decimalnumber = int(decimalnumber)
    octalnumber = j =0
    while (decimalnumber!=0):
        octalnumber = octalnumber + (decimalnumber%8)*(10**j)
        decimalnumber = decimalnumber//8
        j+=1
    print(octalnumber)

#making menus list for options
menu1 = ("A" , "a" , "B" , "b") #menu1 is a list for the inputs that are valid
menu2 = ("A" ,"a", "B" ,"b", "C" ,"c", "D","d") #menu2 is a list for the inputs that are valid for user second and third input
while True :
    print("**numbering system converter**")
    print ("A) insert a new number")
    print("B) exit program")
    user_input = input("please select an option: ")
    if user_input in menu1 :    #user_input --> is the user first input
        break
    else :
        print ("please select a valid option")
if user_input == "A" or user_input == "a":
    number = input("enter a new number: ")
    while True :
        print ("select the base you want to convert from")
        print("A) decimal")
        print("B) binary")
        print("C) octal")
        print("D) hexadecimal")
        user_2input = input("please select an option: ") #user_2input --> is the user second input
        if user_2input in menu2:
            break
        else :
            print("please select a valid option")
    while True :
        print("select the base you want to convert to")
        print("A) decimal")
        print("B) binary")
        print("C) octal")
        print("D) hexadecimal")
        user_3input = input("please select an option: ") #user_3input --> is the user third input
        if user_3input in menu2 :
            break
        else :
            print("please select a valid option")
    if user_2input == "A" or user_2input == "a":
        if checkdecimal:
            if user_3input == "A" or user_3input == "a": #if user converted from decimal to decimal
                print(number , "is already in decimal")
            elif user_3input == "B" or user_3input == "b": #if user converted from decimal to binary
                print(decimaltobinary(number))
            elif user_3input == "C" or user_3input == "c": #if user converted from decimal to octal
                print(decimaltooctal(number))
            elif user_3input == "D" or user_3input == "d": #if user converted from decimal to hexadecimal
                print(decimaltohexadecimal(number))   
        else :
            print("the number you entered isn't decimal") #if user choose a wrong base for the number he entered
    elif user_2input == "B" or user_2input == "b" :
        if checkbinary:
            if user_3input == "A" or user_3input == "a": #if user converted from binary to decimal
                print(binarytodecimal(number))
            elif user_3input == "B" or user_3input == "b": #if user converted from binary to binary
                print(number , "is already in binary")
            elif user_3input == "C" or user_3input == "c": #if user converted from binary to octal
                print(binarytooctal(number))
            elif user_3input == "D" or user_3input == "d": #if user converted from binary to hexadecimal
                print(binarytohexadecimal(number))
        else :
            print("the number you entered isn't binary") #if user choose a wrong base for the number he entered
    elif user_2input == "C" or user_2input == "c":
        if checkoctal:
            if user_3input == "A" or user_3input == "a": #if user converted from octal to decimal
                print(octaltodecimal(number))
            elif user_3input == "B" or user_3input == "b": #if user converted from octal to binary
                print(octaltobinary(number))
            elif user_3input == "C" or user_3input == "c": #if user converted from octal to octal
                print(number , "is already in octal")    
            elif user_3input == "D" or user_3input == "d": #if user converted from octal to hexadecimal
                print(octaltohexadecimal(number))
        else :
            print("the number you entered isn't octal") #if user choose a wrong base for the number he entered
    elif user_2input == "D" or user_2input == "d":
        if checkhexadecimal:
            if user_3input == "A" or user_3input == "a": #if user converted from hexadecimal to decimal
                print(hexadecimaltodecimal(number))
            elif user_3input == "B" or user_3input == "b": #if user converted from hexadecimal to binary
                print(hexadecimaltobinary(number))
            elif user_3input == "C" or user_3input == "c": #if user converted from hexadecimal to octal
                print(hexadecimaltooctal(number))
            elif user_3input == "D" or user_3input == "d": #if user converted from hexadecimal to hexadecimal
                print(number , "is already in hexadecimal")
        else:
            print("the number you entered isn't hexadecimal") #if user choose a wrong base for the number he entered

elif user_input == "B" or user_input == "b" : # if the user choose to exit the programm
    print("thank you for using numbering system converter")


