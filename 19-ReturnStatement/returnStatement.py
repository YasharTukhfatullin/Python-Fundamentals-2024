"""
return statement = functions send Python values/objects back to the caller.
                  These values/object are known as the function's return value.
"""


def multiply(num1, num2):
    result = num1 * num2
    return result


print(multiply(2, 2))
print("============")


def short_multiply(num1, num2):
    return num1 * num2


print(multiply(3, 3))
