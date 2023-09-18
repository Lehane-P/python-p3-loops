#!/usr/bin/env python3




def happy_new_year():
    # code goes here!
    number = 10
    while number >= 1:
        print(number)
        number -= 1
    print ("Happy New Year!")


happy_new_year()
pass


def square_integers(int_list):
    # code goes here!
    squared_element = []
    for number in int_list:
        squared_element.append(number ** 2)

    return squared_element    

    pass

# Sample test case

test_list = [1, 2, 5, 7, 8, 200, 40]
result = square_integers(test_list)
print(result)




def fizzbuzz():
    # code goes here!
    for number in range(1, 101):  
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizzbuzz()


