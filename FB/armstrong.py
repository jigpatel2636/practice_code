def Armstrong(n):
    total = 0
    if len(str(n)) == 1 :
        return f"{n} is armstrong number"
    elif len(str(n)) > 1:
        for i in str(n):
            total += int(i)**len(str(n))
        if total == n:
            print("Number is Armstrong ")
        else:
            print("Number is not armstrong")
    else:
        return "Number is not valid"

def findarmstrong(n):

    for i in range(n):
        result = 0
        num = i
        n = len(str(i))
        while i !=0:
            digit = i%10
            result = result + digit**n
            i = i//10
        if result == num:
            print(num)

findarmstrong(1001)





