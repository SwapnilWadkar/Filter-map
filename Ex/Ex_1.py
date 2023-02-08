try:
    userinput = input("Enter the number = ")
    result = 100/int(userinput)
    print(result)
except ValueError:
    print("not a number,Please enter a number") 
except ZeroDivisionError:
    print("Please enter a number greater than zero")      