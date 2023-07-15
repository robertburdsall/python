# return statement - used within function to send values or objects back to the caller
# those objects/values are known as the function's return value

def multiply(number1, number2):
    result = number1 * number2
    return result
# or you could do return number1 * number2


#print(multiply(6, 8))

x = multiply(6, 8)

print(x)