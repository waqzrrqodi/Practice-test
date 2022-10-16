# def age_after_hundred(age):
#     name = input("What is your name? ")
#     age_in_hundred = 2022 + 100 - age
#     print(f"{name}, you will be 100 years old in the year {age_in_hundred}")

# age_after_hundred(int(input("How old are you?")))

# from itertools import count


# def count_42(numbers):
#     how_many = numbers.count(42)
#     print(f"Det finns {how_many} st 42 i listan")

# count_42([1,2,5,2,42,42,42,42])



def test_number(number):
    if number > 265 and number % 34 == 4:
        return True
    else:
        return False

print(test_number(914))