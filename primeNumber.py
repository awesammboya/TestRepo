#  This program checks if a number  is a a prime or not.
num = 407;
# To take input from the user
# num =int(input("ENter a number: "))

#Define a flag variable
flag = False;
# prime numbers greater than 1
if num > 1:
    for i in range(2,num):
        if (num % i)== 0:
        #if factor is found, set flag to True
            flag = True
        break

# Check if the flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

