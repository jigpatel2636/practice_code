netmask = "255.255.255.240"
total = 0
for i in netmask.split("."):
    print(bin(int(i)))
    print(bin(int(i)).count('1'))
    total += bin(int(i)).count('1')
print(total)