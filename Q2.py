num=int(input("Enter number :"))
for n in range(2,num):
    if (num % n)==0:
        print("the given number (",num,") is not prime number.")
        break
else:
    print("the given number (",num,") is prime number.")
