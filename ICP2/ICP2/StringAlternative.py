def string_alternative(Str, length):  #function defination of string_alternative
    for x in range(length):
        if x%2 == 0:                   # checking the index is even or odd
            print(Str[x], end =" ")      # printing the result in same line


def main(Str, length):                 # function defination of main
  print("In Main")
  string_alternative(Str, length)         # calling string_alternative function with parameters


Str = input("enter the string")          # reading input string
length = len(Str)
print(length)
main(Str, length)                        # calling main




