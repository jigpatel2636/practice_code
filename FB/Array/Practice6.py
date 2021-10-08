def plusOne(digits):
    # z = digits
    x = digits.pop() + 1
    digits.append(x)
    print(digits)

x = [1,2,3]
plusOne(x)