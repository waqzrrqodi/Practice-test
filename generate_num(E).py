def numbers_between(tal1, tal2):
    x = tal1 + 1
    while x < tal2:
        print(x)
        x += 1

numbers_between(int(input("Skriv ett tal: ")), int(input("Skriv ett annat högre tal: ")))