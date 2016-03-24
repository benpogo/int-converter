def new_line(): # function definition for creating a new line in output
    print

userval = int(input("Please enter a number between 0 and 255:")) # takes in user input

print ("RESULTS")
print ("-------")
new_line()
print ("Decimal: ")
print (userval) # prints the decimal value
new_line()
print ("Binary: ")
print (bin(userval)[2:]) # converts the decimal value to binary and prints it
new_line()
print ("Hex: ")
print (hex(userval)[2:]) # converts the decimal value to hex and prints it
