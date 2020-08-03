readinput = input("Enter Python")    # reading input from console
deleteinput = readinput.replace("n","").replace("o","")  # replace n and o with blank
print("output is "+ deleteinput[::-1])             # reverse the string

read1 = int(input("enter one number"))  # reading input from console
read2 = int(input("enter second number"))  # reading another input from console
print( read1 + read2)       # add the two inputs and print the result


