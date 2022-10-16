i = 1

while i < 101:
    temp_string = ""
    if i % 3 == 0:
        temp_string = temp_string + "Fizz"
    if i % 5 == 0:
        temp_string = temp_string + "Buzz"

    if temp_string == "":
        print(i)
    else:
        print(temp_string)
    i += 1