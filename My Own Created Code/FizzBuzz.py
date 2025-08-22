def fizzbuzz():
    count = 0
    index = 0
    number = []

    for count in range(1,101):
        number.append(count)

    for index in range(0, len(number)):
        if number[index] % 15 == 0:
            print("Fizzbuzz")
        
        elif number[index] % 5 == 0:
            print("Buzz")
        
        elif number[index] % 3 == 0:
            print("Fizz")
        
        else:
            print(number[index])
        index = index + 1
fizzbuzz()