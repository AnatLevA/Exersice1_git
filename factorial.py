num = input("please enter a positive real number\n")

def factorial_func(x):
   if x==0:
       return 1
   else:
       return x*factorial_func(x-1)



outcome=factorial_func(num)
print("the factorial of the number " + str(num) + " is " + str(outcome))
