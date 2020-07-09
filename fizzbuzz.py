x = range(0,101)
def FizzBuzz(list):
    for num in list:
        if num %3 == 0 and num % 5 == 0:
            print("FIZZBUZZ")
        elif num % 3 ==0 :
            print("FIZZ")
        elif num % 5 == 0:
            print("Buzz")
        else :
            print(num)
FizzBuzz(x)